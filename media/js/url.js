function set_url(id){
    url = "/gallery/" + id + "/";
    if ( typeof(history.pushState) == 'function' ) { history.pushState({id: id}, "Page", url);}
    else { window.location = url; }
}
function set_img(url){
    image = document.getElementById("photo");
    image.src=url;
    return false;
}

function getXmlHttp(){
    var isMSIE = /*@cc_on!@*/false;
    var xmlhttp;
    if (isMSIE) {   try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
            xmlhttp = false;
            }
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function set_content(id){
    title = document.getElementById("hand_title");
    content = document.getElementById("hand_txt");
    var xmlhttp = getXmlHttp();
    xmlhttp.open('GET', '/gallery/title_by_id/'+id+'/', false);
    xmlhttp.send(null);
    title.innerHTML = xmlhttp.responseText;
    document.getElementsByTagName("title")[0].innerHTML = xmlhttp.responseText;

    xmlhttp.open('GET', '/gallery/content_by_id/'+id+'/', false);
    xmlhttp.send(null);
    content.innerHTML = xmlhttp.responseText ;
}

function get_url(id){
    return img_urls[id]
}

function list_counter(PhotoList, page){
    if(PhotoList === undefined)
        throw("no photo list");

    for(item in PhotoList){
        if(PhotoList[item] == page){
            this.counter = item;
        };
    };
    if(this.counter === undefined){
        this.counter = 0
    };
    var self = this;

    this.current = function(){
         return PhotoList[self.counter];
    };

    this.next = function(){
        self.counter++
        n = PhotoList[self.counter];
        if(n === undefined) { n = PhotoList[0]; self.counter = 0;}
        set_img(get_url(n));
        set_url(n);
        set_content(n);
        return false;
    };

    this.prev = function(){
        self.counter--
        n = PhotoList[self.counter];
        l = PhotoList.length - 1;
        if(n === undefined) { n = PhotoList[l]; self.counter = l - 1; }
        set_img(get_url(n));
        set_url(n);
        set_content(n);
        return false;
    };

}

window.addEventListener('popstate', function(e){
    if( e.state ){
        if(e.state.id) {
            set_img(get_url(e.state.id));
            //set_url(e.state.id);
            set_content(e.state.id);
            e.preventDefault();
        }
    }
}, false);
