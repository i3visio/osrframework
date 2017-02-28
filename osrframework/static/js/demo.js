;window.Modernizr=function(a,b,c){function A(a){j.cssText=a}function B(a,b){return A(m.join(a+";")+(b||""))}function C(a,b){return typeof a===b}function D(a,b){return!!~(""+a).indexOf(b)}function E(a,b){for(var d in a){var e=a[d];if(!D(e,"-")&&j[e]!==c)return b=="pfx"?e:!0}return!1}function F(a,b,d){for(var e in a){var f=b[a[e]];if(f!==c)return d===!1?a[e]:C(f,"function")?f.bind(d||b):f}return!1}function G(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),e=(a+" "+o.join(d+" ")+d).split(" ");return C(b,"string")||C(b,"undefined")?E(e,b):(e=(a+" "+p.join(d+" ")+d).split(" "),F(e,b,c))}var d="2.7.1",e={},f=!0,g=b.documentElement,h="modernizr",i=b.createElement(h),j=i.style,k,l={}.toString,m=" -webkit- -moz- -o- -ms- ".split(" "),n="Webkit Moz O ms",o=n.split(" "),p=n.toLowerCase().split(" "),q={svg:"http://www.w3.org/2000/svg"},r={},s={},t={},u=[],v=u.slice,w,x=function(a,c,d,e){var f,i,j,k,l=b.createElement("div"),m=b.body,n=m||b.createElement("body");if(parseInt(d,10))while(d--)j=b.createElement("div"),j.id=e?e[d]:h+(d+1),l.appendChild(j);return f=["&#173;",'<style id="s',h,'">',a,"</style>"].join(""),l.id=h,(m?l:n).innerHTML+=f,n.appendChild(l),m||(n.style.background="",n.style.overflow="hidden",k=g.style.overflow,g.style.overflow="hidden",g.appendChild(n)),i=c(l,a),m?l.parentNode.removeChild(l):(n.parentNode.removeChild(n),g.style.overflow=k),!!i},y={}.hasOwnProperty,z;!C(y,"undefined")&&!C(y.call,"undefined")?z=function(a,b){return y.call(a,b)}:z=function(a,b){return b in a&&C(a.constructor.prototype[b],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(b){var c=this;if(typeof c!="function")throw new TypeError;var d=v.call(arguments,1),e=function(){if(this instanceof e){var a=function(){};a.prototype=c.prototype;var f=new a,g=c.apply(f,d.concat(v.call(arguments)));return Object(g)===g?g:f}return c.apply(b,d.concat(v.call(arguments)))};return e}),r.touch=function(){var c;return"ontouchstart"in a||a.DocumentTouch&&b instanceof DocumentTouch?c=!0:x(["@media (",m.join("touch-enabled),("),h,")","{#modernizr{top:9px;position:absolute}}"].join(""),function(a){c=a.offsetTop===9}),c},r.cssanimations=function(){return G("animationName")},r.csstransitions=function(){return G("transition")},r.svg=function(){return!!b.createElementNS&&!!b.createElementNS(q.svg,"svg").createSVGRect},r.inlinesvg=function(){var a=b.createElement("div");return a.innerHTML="<svg/>",(a.firstChild&&a.firstChild.namespaceURI)==q.svg};for(var H in r)z(r,H)&&(w=H.toLowerCase(),e[w]=r[H](),u.push((e[w]?"":"no-")+w));return e.addTest=function(a,b){if(typeof a=="object")for(var d in a)z(a,d)&&e.addTest(d,a[d]);else{a=a.toLowerCase();if(e[a]!==c)return e;b=typeof b=="function"?b():b,typeof f!="undefined"&&f&&(g.className+=" "+(b?"":"no-")+a),e[a]=b}return e},A(""),i=k=null,function(a,b){function l(a,b){var c=a.createElement("p"),d=a.getElementsByTagName("head")[0]||a.documentElement;return c.innerHTML="x<style>"+b+"</style>",d.insertBefore(c.lastChild,d.firstChild)}function m(){var a=s.elements;return typeof a=="string"?a.split(" "):a}function n(a){var b=j[a[h]];return b||(b={},i++,a[h]=i,j[i]=b),b}function o(a,c,d){c||(c=b);if(k)return c.createElement(a);d||(d=n(c));var g;return d.cache[a]?g=d.cache[a].cloneNode():f.test(a)?g=(d.cache[a]=d.createElem(a)).cloneNode():g=d.createElem(a),g.canHaveChildren&&!e.test(a)&&!g.tagUrn?d.frag.appendChild(g):g}function p(a,c){a||(a=b);if(k)return a.createDocumentFragment();c=c||n(a);var d=c.frag.cloneNode(),e=0,f=m(),g=f.length;for(;e<g;e++)d.createElement(f[e]);return d}function q(a,b){b.cache||(b.cache={},b.createElem=a.createElement,b.createFrag=a.createDocumentFragment,b.frag=b.createFrag()),a.createElement=function(c){return s.shivMethods?o(c,a,b):b.createElem(c)},a.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+m().join().replace(/[\w\-]+/g,function(a){return b.createElem(a),b.frag.createElement(a),'c("'+a+'")'})+");return n}")(s,b.frag)}function r(a){a||(a=b);var c=n(a);return s.shivCSS&&!g&&!c.hasCSS&&(c.hasCSS=!!l(a,"article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}mark{background:#FF0;color:#000}template{display:none}")),k||q(a,c),a}var c="3.7.0",d=a.html5||{},e=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,f=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,g,h="_html5shiv",i=0,j={},k;(function(){try{var a=b.createElement("a");a.innerHTML="<xyz></xyz>",g="hidden"in a,k=a.childNodes.length==1||function(){b.createElement("a");var a=b.createDocumentFragment();return typeof a.cloneNode=="undefined"||typeof a.createDocumentFragment=="undefined"||typeof a.createElement=="undefined"}()}catch(c){g=!0,k=!0}})();var s={elements:d.elements||"abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output progress section summary template time video",version:c,shivCSS:d.shivCSS!==!1,supportsUnknownElements:k,shivMethods:d.shivMethods!==!1,type:"default",shivDocument:r,createElement:o,createDocumentFragment:p};a.html5=s,r(b)}(this,b),e._version=d,e._prefixes=m,e._domPrefixes=p,e._cssomPrefixes=o,e.testProp=function(a){return E([a])},e.testAllProps=G,e.testStyles=x,g.className=g.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(f?" js "+u.join(" "):""),e}(this,this.document),function(a,b,c){function d(a){return"[object Function]"==o.call(a)}function e(a){return"string"==typeof a}function f(){}function g(a){return!a||"loaded"==a||"complete"==a||"uninitialized"==a}function h(){var a=p.shift();q=1,a?a.t?m(function(){("c"==a.t?B.injectCss:B.injectJs)(a.s,0,a.a,a.x,a.e,1)},0):(a(),h()):q=0}function i(a,c,d,e,f,i,j){function k(b){if(!o&&g(l.readyState)&&(u.r=o=1,!q&&h(),l.onload=l.onreadystatechange=null,b)){"img"!=a&&m(function(){t.removeChild(l)},50);for(var d in y[c])y[c].hasOwnProperty(d)&&y[c][d].onload()}}var j=j||B.errorTimeout,l=b.createElement(a),o=0,r=0,u={t:d,s:c,e:f,a:i,x:j};1===y[c]&&(r=1,y[c]=[]),"object"==a?l.data=c:(l.src=c,l.type=a),l.width=l.height="0",l.onerror=l.onload=l.onreadystatechange=function(){k.call(this,r)},p.splice(e,0,u),"img"!=a&&(r||2===y[c]?(t.insertBefore(l,s?null:n),m(k,j)):y[c].push(l))}function j(a,b,c,d,f){return q=0,b=b||"j",e(a)?i("c"==b?v:u,a,b,this.i++,c,d,f):(p.splice(this.i++,0,a),1==p.length&&h()),this}function k(){var a=B;return a.loader={load:j,i:0},a}var l=b.documentElement,m=a.setTimeout,n=b.getElementsByTagName("script")[0],o={}.toString,p=[],q=0,r="MozAppearance"in l.style,s=r&&!!b.createRange().compareNode,t=s?l:n.parentNode,l=a.opera&&"[object Opera]"==o.call(a.opera),l=!!b.attachEvent&&!l,u=r?"object":l?"script":"img",v=l?"script":u,w=Array.isArray||function(a){return"[object Array]"==o.call(a)},x=[],y={},z={timeout:function(a,b){return b.length&&(a.timeout=b[0]),a}},A,B;B=function(a){function b(a){var a=a.split("!"),b=x.length,c=a.pop(),d=a.length,c={url:c,origUrl:c,prefixes:a},e,f,g;for(f=0;f<d;f++)g=a[f].split("="),(e=z[g.shift()])&&(c=e(c,g));for(f=0;f<b;f++)c=x[f](c);return c}function g(a,e,f,g,h){var i=b(a),j=i.autoCallback;i.url.split(".").pop().split("?").shift(),i.bypass||(e&&(e=d(e)?e:e[a]||e[g]||e[a.split("/").pop().split("?")[0]]),i.instead?i.instead(a,e,f,g,h):(y[i.url]?i.noexec=!0:y[i.url]=1,f.load(i.url,i.forceCSS||!i.forceJS&&"css"==i.url.split(".").pop().split("?").shift()?"c":c,i.noexec,i.attrs,i.timeout),(d(e)||d(j))&&f.load(function(){k(),e&&e(i.origUrl,h,g),j&&j(i.origUrl,h,g),y[i.url]=2})))}function h(a,b){function c(a,c){if(a){if(e(a))c||(j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}),g(a,j,b,0,h);else if(Object(a)===a)for(n in m=function(){var b=0,c;for(c in a)a.hasOwnProperty(c)&&b++;return b}(),a)a.hasOwnProperty(n)&&(!c&&!--m&&(d(j)?j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}:j[n]=function(a){return function(){var b=[].slice.call(arguments);a&&a.apply(this,b),l()}}(k[n])),g(a[n],j,b,n,h))}else!c&&l()}var h=!!a.test,i=a.load||a.both,j=a.callback||f,k=j,l=a.complete||f,m,n;c(h?a.yep:a.nope,!!i),i&&c(i)}var i,j,l=this.yepnope.loader;if(e(a))g(a,0,l,0);else if(w(a))for(i=0;i<a.length;i++)j=a[i],e(j)?g(j,0,l,0):w(j)?B(j):Object(j)===j&&h(j,l);else Object(a)===a&&h(a,l)},B.addPrefix=function(a,b){z[a]=b},B.addFilter=function(a){x.push(a)},B.errorTimeout=1e4,null==b.readyState&&b.addEventListener&&(b.readyState="loading",b.addEventListener("DOMContentLoaded",A=function(){b.removeEventListener("DOMContentLoaded",A,0),b.readyState="complete"},0)),a.yepnope=k(),a.yepnope.executeStack=h,a.yepnope.injectJs=function(a,c,d,e,i,j){var k=b.createElement("script"),l,o,e=e||B.errorTimeout;k.src=a;for(o in d)k.setAttribute(o,d[o]);c=j?h:c||f,k.onreadystatechange=k.onload=function(){!l&&g(k.readyState)&&(l=1,c(),k.onload=k.onreadystatechange=null)},m(function(){l||(l=1,c(1))},e),i?k.onload():n.parentNode.insertBefore(k,n)},a.yepnope.injectCss=function(a,c,d,e,g,i){var e=b.createElement("link"),j,c=i?h:c||f;e.href=a,e.rel="stylesheet",e.type="text/css";for(j in d)e.setAttribute(j,d[j]);g||(n.parentNode.insertBefore(e,n),m(c,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};

// turn on social share by default
var socialShare = false;
// turn on rubbon by default
var noRibbon = false;
var showLogo = false;
var githubButton = false;

function resizeBrowser(minWidth, minHeight){
    if(minWidth) $('#chart_div').width($(window).width()-minWidth);
    if(minHeight) $('#chart_div').height($(window).height()-minHeight);
};

var getIcon = function(v){
    var iconName="";
    switch(v.toLowerCase()){
        case "male": 
        case "m": 
            iconName = "male"; break;
        case "female": 
        case "f": 
            iconName = "female"; break;
        case "organization": 
            iconName = "university"; break;
        case "medicine": 
            iconName = "stethoscope"; break;
        case "economics": 
            iconName = "money"; break;
        case "literature": 
            iconName = "book"; break;
        case "physics": 
            iconName = "bolt"; break;
        case "chemistry": 
            iconName = "flask"; break;
        case "peace": 
            iconName = "flag-o"; break;
    }
    return "<span class='fa fa-"+iconName+"'></span>";
};

var getStateName = function(v){
    switch(v){
        case 'AL': return 'Alabama';
        case 'AK': return 'Alaska';
        case 'AZ': return 'Arizona';
        case 'AR': return 'Arkansas';
        case 'CA': return 'California';
        case 'CO': return 'Colorado';
        case 'CT': return 'Connecticut';
        case 'DE': return 'Delaware';
        case 'DC': return 'District of Columbia';
        case 'FL': return 'Florida';
        case 'GA': return 'Georgia';
        case 'HI': return 'Hawaii';
        case 'ID': return 'Idaho';
        case 'IL': return 'Illinois';
        case 'IN': return 'Indiana';
        case 'IA': return 'Iowa';
        case 'KS': return 'Kansas';
        case 'KY': return 'Kentucky';
        case 'LA': return 'Louisiana';
        case 'ME': return 'Maine';
        case 'MD': return 'Maryland';
        case 'MA': return 'Massachusetts';
        case 'MI': return 'Michigan';
        case 'MN': return 'Minnesota';
        case 'MS': return 'Mississippi';
        case 'MO': return 'Missouri';
        case 'MT': return 'Montana';
        case 'NE': return 'Nebraska';
        case 'NV': return 'Nevada';
        case 'NH': return 'New Hampshire';
        case 'NJ': return 'New Jersey';
        case 'NM': return 'New Mexico';
        case 'NY': return 'New York';
        case 'NC': return 'North Carolina';
        case 'ND': return 'North Dakota';
        case 'OH': return 'Ohio';
        case 'OK': return 'Oklahoma';
        case 'OR': return 'Oregon';
        case 'PA': return 'Pennsylvania';
        case 'RI': return 'Rhode Island';
        case 'SC': return 'South Carolina';
        case 'SD': return 'South Dakota';
        case 'TN': return 'Tennessee';
        case 'TX': return 'Texas';
        case 'UT': return 'Utah';
        case 'VT': return 'Vermont';
        case 'VA': return 'Virginia';
        case 'WA': return 'Washington';
        case 'WV': return 'West Virginia';
        case 'WI': return 'Wisconsin';
        case 'WY': return 'Wyoming';
        case 'PR': return 'Puerto-Rico';
        case 'VI': return 'Virgin Islands';
        case 'GU': return 'GUAM';
        default  : return 'Unknown: '+v;
    }
};

function getMonthNameFromNumber(v){
    switch(v){
        case 0:  return "January";
        case 1:  return "February";
        case 2:  return "March";
        case 3:  return "April";
        case 4:  return "May";
        case 5:  return "June";
        case 6:  return "July";
        case 7:  return "August";
        case 8:  return "September";
        case 9:  return "October";
        case 10: return "November";
        case 11: return "December";
    }
    return "?";
};


function getDayNameFromNumber(v){
    switch(v){
        case 1: return "Monday";
        case 2: return "Tuesday";
        case 3: return "Wednesday";
        case 4: return "Thursday";
        case 5: return "Friday";
        case 6: return "Saturday";
        case 0: return "Sunday";
    }
    return "?";
};

function getMonthNumberFromName(v){
    switch(v){
        case "January"  : return 0;
        case "February" : return 1;
        case "March"    : return 2;
        case "April"    : return 3;
        case "May"      : return 4;
        case "June"     : return 5;
        case "July"     : return 6;
        case "August"   : return 7;
        case "September": return 8;
        case "October"  : return 9;
        case "November" : return 10;
        case "December" : return 11;
        default         : return 12;
    }
};

// Based on ISO_3166 codes
function getCountryName(v){
    switch(v){
        case 'AD': return "Andorra";
        case 'AE': return "United Arab Emirates";
        case 'AF': return "Afghanistan";
        case 'AG': return "Antigua and Barbuda";
        case 'AI': return "Anguilla";
        case 'AL': return "Albania";
        case 'AM': return "Armenia";
        case 'AO': return "Angola";
        case 'AQ': return "Antarctica";
        case 'AR': return "Argentina";
        case 'AS': return "American Samoa";
        case 'AT': return "Austria";
        case 'AU': return "Australia";
        case 'AW': return "Aruba";
        case 'AX': return "Åland Islands";
        case 'AZ': return "Azerbaijan";
        case 'BA': return "Bosnia and Herzegovina";
        case 'BB': return "Barbados";
        case 'BD': return "Bangladesh";
        case 'BE': return "Belgium";
        case 'BF': return "Burkina Faso";
        case 'BG': return "Bulgaria";
        case 'BH': return "Bahrain";
        case 'BI': return "Burundi";
        case 'BJ': return "Benin";
        case 'BL': return "Saint Barthélemy";
        case 'BM': return "Bermuda";
        case 'BN': return "Brunei Darussalam";
        case 'BO': return "Bolivia, Plurinational State of";
        case 'BQ': return "Bonaire, Sint Eustatius and Saba";
        case 'BR': return "Brazil";
        case 'BS': return "Bahamas";
        case 'BT': return "Bhutan";
        case 'BV': return "Bouvet Island";
        case 'BW': return "Botswana";
        case 'BY': return "Belarus";
        case 'BZ': return "Belize";
        case 'CA': return "Canada";
        case 'CC': return "Cocos (Keeling) Islands";
        case 'CD': return "Congo, the Democratic Republic of the";
        case 'CF': return "Central African Republic";
        case 'CG': return "Congo";
        case 'CH': return "Switzerland";
        case 'CI': return "Côte d'Ivoire";
        case 'CK': return "Cook Islands";
        case 'CL': return "Chile";
        case 'CM': return "Cameroon";
        case 'CN': return "China";
        case 'CO': return "Colombia";
        case 'CR': return "Costa Rica";
        case 'CU': return "Cuba";
        case 'CV': return "Cabo Verde";
        case 'CW': return "Curaçao";
        case 'CX': return "Christmas Island";
        case 'CY': return "Cyprus";
        case 'CZ': return "Czech Republic";
        case 'DE': return "Germany";
        case 'DJ': return "Djibouti";
        case 'DK': return "Denmark";
        case 'DM': return "Dominica";
        case 'DO': return "Dominican Republic";
        case 'DZ': return "Algeria";
        case 'EC': return "Ecuador";
        case 'EE': return "Estonia";
        case 'EG': return "Egypt";
        case 'EH': return "Western Sahara";
        case 'ER': return "Eritrea";
        case 'ES': return "Spain";
        case 'ET': return "Ethiopia";
        case 'FI': return "Finland";
        case 'FJ': return "Fiji";
        case 'FK': return "Falkland Islands (Malvinas)";
        case 'FM': return "Micronesia, Federated States of";
        case 'FO': return "Faroe Islands";
        case 'FR': return "France";
        case 'GA': return "Gabon";
        case 'GB': return "United Kingdom of Great Britain and Northern Ireland";
        case 'GD': return "Grenada";
        case 'GE': return "Georgia";
        case 'GF': return "French Guiana";
        case 'GG': return "Guernsey";
        case 'GH': return "Ghana";
        case 'GI': return "Gibraltar";
        case 'GL': return "Greenland";
        case 'GM': return "Gambia";
        case 'GN': return "Guinea";
        case 'GP': return "Guadeloupe";
        case 'GQ': return "Equatorial Guinea";
        case 'GR': return "Greece";
        case 'GS': return "South Georgia and the South Sandwich Islands";
        case 'GT': return "Guatemala";
        case 'GU': return "Guam";
        case 'GW': return "Guinea-Bissau";
        case 'GY': return "Guyana";
        case 'HK': return "Hong Kong";
        case 'HM': return "Heard Island and McDonald Islands";
        case 'HN': return "Honduras";
        case 'HR': return "Croatia";
        case 'HT': return "Haiti";
        case 'HU': return "Hungary";
        case 'ID': return "Indonesia";
        case 'IE': return "Ireland";
        case 'IL': return "Israel";
        case 'IM': return "Isle of Man";
        case 'IN': return "India";
        case 'IO': return "British Indian Ocean Territory";
        case 'IQ': return "Iraq";
        case 'IR': return "Iran, Islamic Republic of";
        case 'IS': return "Iceland";
        case 'IT': return "Italy";
        case 'JE': return "Jersey";
        case 'JM': return "Jamaica";
        case 'JO': return "Jordan";
        case 'JP': return "Japan";
        case 'KE': return "Kenya";
        case 'KG': return "Kyrgyzstan";
        case 'KH': return "Cambodia";
        case 'KI': return "Kiribati";
        case 'KM': return "Comoros";
        case 'KN': return "Saint Kitts and Nevis";
        case 'KP': return "Korea, Democratic People's Republic of";
        case 'KR': return "Korea, Republic of";
        case 'KW': return "Kuwait";
        case 'KY': return "Cayman Islands";
        case 'KZ': return "Kazakhstan";
        case 'LA': return "Lao People's Democratic Republic";
        case 'LB': return "Lebanon";
        case 'LC': return "Saint Lucia";
        case 'LI': return "Liechtenstein";
        case 'LK': return "Sri Lanka";
        case 'LR': return "Liberia";
        case 'LS': return "Lesotho";
        case 'LT': return "Lithuania";
        case 'LU': return "Luxembourg";
        case 'LV': return "Latvia";
        case 'LY': return "Libya";
        case 'MA': return "Morocco";
        case 'MC': return "Monaco";
        case 'MD': return "Moldova, Republic of";
        case 'ME': return "Montenegro";
        case 'MF': return "Saint Martin (French part)";
        case 'MG': return "Madagascar";
        case 'MH': return "Marshall Islands";
        case 'MK': return "Macedonia, the former Yugoslav Republic of";
        case 'ML': return "Mali";
        case 'MM': return "Myanmar";
        case 'MN': return "Mongolia";
        case 'MO': return "Macao";
        case 'MP': return "Northern Mariana Islands";
        case 'MQ': return "Martinique";
        case 'MR': return "Mauritania";
        case 'MS': return "Montserrat";
        case 'MT': return "Malta";
        case 'MU': return "Mauritius";
        case 'MV': return "Maldives";
        case 'MW': return "Malawi";
        case 'MX': return "Mexico";
        case 'MY': return "Malaysia";
        case 'MZ': return "Mozambique";
        case 'NA': return "Namibia";
        case 'NC': return "New Caledonia";
        case 'NE': return "Niger";
        case 'NF': return "Norfolk Island";
        case 'NG': return "Nigeria";
        case 'NI': return "Nicaragua";
        case 'NL': return "Netherlands";
        case 'NO': return "Norway";
        case 'NP': return "Nepal";
        case 'NR': return "Nauru";
        case 'NU': return "Niue";
        case 'NZ': return "New Zealand";
        case 'OM': return "Oman";
        case 'PA': return "Panama";
        case 'PE': return "Peru";
        case 'PF': return "French Polynesia";
        case 'PG': return "Papua New Guinea";
        case 'PH': return "Philippines";
        case 'PK': return "Pakistan";
        case 'PL': return "Poland";
        case 'PM': return "Saint Pierre and Miquelon";
        case 'PN': return "Pitcairn";
        case 'PR': return "Puerto Rico";
        case 'PS': return "Palestine, State of";
        case 'PT': return "Portugal";
        case 'PW': return "Palau";
        case 'PY': return "Paraguay";
        case 'QA': return "Qatar";
        case 'RE': return "Réunion";
        case 'RO': return "Romania";
        case 'RS': return "Serbia";
        case 'RU': return "Russian Federation";
        case 'RW': return "Rwanda";
        case 'SA': return "Saudi Arabia";
        case 'SB': return "Solomon Islands";
        case 'SC': return "Seychelles";
        case 'SD': return "Sudan";
        case 'SE': return "Sweden";
        case 'SG': return "Singapore";
        case 'SH': return "Saint Helena, Ascension and Tristan da Cunha";
        case 'SI': return "Slovenia";
        case 'SJ': return "Svalbard and Jan Mayen";
        case 'SK': return "Slovakia";
        case 'SL': return "Sierra Leone";
        case 'SM': return "San Marino";
        case 'SN': return "Senegal";
        case 'SO': return "Somalia";
        case 'SR': return "Suriname";
        case 'SS': return "South Sudan";
        case 'ST': return "Sao Tome and Principe";
        case 'SV': return "El Salvador";
        case 'SX': return "Sint Maarten (Dutch part)";
        case 'SY': return "Syrian Arab Republic";
        case 'SZ': return "Swaziland";
        case 'TC': return "Turks and Caicos Islands";
        case 'TD': return "Chad";
        case 'TF': return "French Southern Territories";
        case 'TG': return "Togo";
        case 'TH': return "Thailand";
        case 'TJ': return "Tajikistan";
        case 'TK': return "Tokelau";
        case 'TL': return "Timor-Leste";
        case 'TM': return "Turkmenistan";
        case 'TN': return "Tunisia";
        case 'TO': return "Tonga";
        case 'TR': return "Turkey";
        case 'TT': return "Trinidad and Tobago";
        case 'TV': return "Tuvalu";
        case 'TW': return "Taiwan, Province of China";
        case 'TZ': return "Tanzania, United Republic of";
        case 'UA': return "Ukraine";
        case 'UG': return "Uganda";
        case 'UM': return "United States Minor Outlying Islands";
        case 'US': return "United States of America";
        case 'UY': return "Uruguay";
        case 'UZ': return "Uzbekistan";
        case 'VA': return "Holy See";
        case 'VC': return "Saint Vincent and the Grenadines";
        case 'VE': return "Venezuela, Bolivarian Republic of";
        case 'VG': return "Virgin Islands, British";
        case 'VI': return "Virgin Islands, U.S.";
        case 'VN': return "Viet Nam";
        case 'VU': return "Vanuatu";
        case 'WF': return "Wallis and Futuna";
        case 'WS': return "Samoa";
        case 'YE': return "Yemen";
        case 'YT': return "Mayotte";
        case 'ZA': return "South Africa";
        case 'ZM': return "Zambia";
        case 'ZW': return "Zimbabwe";
        default  : return "Unkown: "+v;
    }
}

function writeCookie(name,value,days){
    var date, expires;
    if (days) {
        date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires=" + date.toGMTString();
    }else{
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
};

function readCookie(name){
    var i, c, ca, nameEQ = name + "=";
    ca = document.cookie.split(';');
    for(i=0;i < ca.length;i++) {
        c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1,c.length);
        }
        if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length,c.length);
        }
    }
    return '';
};

var printPeopleIcons = function(){
    var str="";
    for(var i=0; i<this.id; i++) str+="<i class='fa fa-male'></i>";
    return str;
};

function noop(){};

// Logging
var isMobile = {
    Android    : function() { return navigator.userAgent.match(/Android/i); },
    BlackBerry : function() { return navigator.userAgent.match(/BlackBerry/i); },
    iOS        : function() { return navigator.userAgent.match(/iPhone|iPad|iPod/i); },
    Opera      : function() { return navigator.userAgent.match(/Opera Mini/i); },
    Windows    : function() { return navigator.userAgent.match(/IEMobile/i); },
    any        : function() {
        return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
    }
};
var logIf = {
    WindowSize : function(){ // minimum 950 x 500 (timeline is shown with 4 categories)
        // Using HTML document size (Device screen.width & screen.height is not important)
        var w=this.dom.width();
        var h=this.dom.height();
        return (w>950) && (h>500) /* && (w>h)*/;
    },
    Desktop : function(){ // skip: Android, Blackberry, iPhone, iPad, iPod, Opera Mini, IEMobile
        return isMobile.any()===null;
    },
    NoTouch : function(){ // skip browsers supporting touch events.
        return !Modernizr.touch; 
    },
    setSessionID : function(t){
        if(this.Check!==undefined) return;
        if(t!==undefined){
            this.dom = $(t);
        }
        document.getElementsByTagName("body")[0].onmousemove = null;
        this.sessionID_Cookie = readCookie('sessionId');
        if(this.sessionID_Cookie === '') {
            var ran  = window.event.clientX*Math.random();
            var ran2 = window.event.clientY*Math.random();
            this.sessionID_Cookie = Math.floor((ran+ran2)*10000000000000);
            writeCookie('sessionId', this.sessionID_Cookie, 365);
        } else {
            this.sessionID_Cookie = parseInt(this.sessionID_Cookie);
        }
        this.sessionID_Now = Math.floor(Math.random()*10000000000000);
        this.All();
    },
    host : function(){
        switch(document.location.hostname){
            case "localhost": return true;
            /*case "adilyalcin.github.io": return true;
            case "www.cs.umd.edu": return true;
            case "cs.umd.edu": return true;
            case "www.keshif.me": return true;
            case "keshif.me": return true;*/
        }
        return false;
    },
    All : function(){
        var tmp = this.Check;
        this.Check = 
            (typeof demoID === 'number') && 
            this.WindowSize() && 
            this.Desktop() && 
            this.NoTouch() && 
            this.host()===true && 
            (this.sessionID_Cookie!==null)
            ;
        if(this.Check===true && tmp === undefined) {
            this.loadTs = Date.now();
            sendLog(kshf.LOG.CONFIG,
                { height:this.dom.height(),width:this.dom.width(),agent:navigator.userAgent}, this.loadTs);
        }
        return this.Check;
    },
    dom: $(window),
    sessionID_Cookie: null,
    sessionID_Now: null,
    Check : undefined,
    loadTs: null,
};

var sendLog = function(actID, dt, ts){
    if(logIf.Check!==true) return;
    if(ts===undefined){ ts = Date.now()-logIf.loadTs; }
    var _dt = {
        'demoID': demoID,
        'actID' : actID,
        'ses_Cki' : logIf.sessionID_Cookie,
        'ses_Now': logIf.sessionID_Now,
        'ts'    : ts,
    };
    // custom data to be sent
    if(dt){ for (var key in dt) { _dt[key]=dt[key]; } }
    $.ajax({
        type: "GET",
        dataType: "jsonp",
        cache: true,
        jsonp: false,
        url: (document.location.hostname!=="localhost")?"http://keshiftracker.appspot.com":"http://localhost:9090/",
        data: _dt
    });
};;

$(window).load(function(){

    if(document.location.hostname!=="localhost"){
        /*(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', 'UA-54042831-2', 'auto');
        ga('send', 'pageview');*/
    }

    if(showLogo){
        /*var keshif_logo = d3.select("body").append("a").attr("class","keshif_logo")
            .attr("href","http://www.keshif.me").attr("target","_blank");
        keshif_logo.append("img").attr("class","keshif_logo_img").attr("src","./img/logo.png");
        keshif_logo.append("span").attr("class","keshif_logo_content").html(
            "<strong>Keshif</strong></br>Data Made Explorable"
        );*/
    }

    if(!noRibbon){
        /*var githubDemoRoot = "https://github.com/adilyalcin/Keshif/blob/master/demo/";
        var pageName = window.location.pathname.split("/");
        pageName = pageName[pageName.length-1];
        if(pageName.indexOf("html")===-1) pageName+=".html";

        /*d3.select("body").append("span").attr("class","forkongithub fork-bottom fork-right")
            .append("a").attr("href","http://www.keshif.me").attr("target","_blank")
            .attr("class","fork-ribbon").html("More <span class='fa fa-bar-chart'></span> ...");

        d3.select("body").append("span").attr("class",'forkongithub fork-bottom fork-left').html(
            "<a class='fork-ribbon' href='"+githubDemoRoot+pageName+"' target='_blank'>"+
                //'<span class="github-button" href="https://github.com/adilyalcin/keshif" data-icon="octicon-star" aria-label="Star adilyalcin/keshif on GitHub"></span>'+
                "<span class='fa fa-star' style='font-size: 1.5em'></span>"+
                " Open Source "+
                "<span class='fa fa-github fa' style='font-size: 1.5em'></span>"+
            "</a>"
        );*/
    }

    if(socialShare===true){
        var s = document.createElement("script");
        s.type = "text/javascript";
        s.src = "//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-534742f736ae906e";
        s.async = "async";
        $("body").append(s);
    }

    d3.select("head").append("link")
        .attr("rel","icon")
        .attr("href","./img/favicon.png")
        .attr("type","image/png");


    if($("body").fancybox && false){

        var com_dom = d3.select("body").append("span").attr("class","comment_popup").attr("href",
            "https://docs.google.com/forms/d/1OohNaCzV42jHFtqTxVaci3CISGiR6znYTvEozFm2z7k/viewform?embedded=true");

        var com_dom_stack = com_dom.append("span").attr("class","fa-stack");
            com_dom_stack.append("i").attr("class","fa fa-stack-1x fa-comment");
            com_dom_stack.append("i").attr("class","fa fa-stack-1x fa-comment-o");
        com_dom.append("br");
        com_dom.append("span").attr("class","texttt").html("Share<br>your<br>feedback");

        $(".comment_popup").fancybox({
            type: 'iframe',
            width: 600,
            height: 300,
            closeBtn: true,
            iframe: { 
                preload: true
            }
        });
    }

    if(githubButton===true){
        var s = document.createElement("script");
        s.src = "https://buttons.github.io/buttons.js";
        s.id  = "github-bjs";
        s.async = "async";
        $("body").append(s);
    }



});

