/*********************************

keshif library

Copyright (c) 2014-2015, University of Maryland
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the University of Maryland nor the names of its contributors
  may not be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL MICHAEL BOSTOCK BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

************************************ */
        

// load google visualization library only if google scripts were included
if(typeof google !== 'undefined'){
    google.load('visualization', '1', {'packages': []});
}

if(typeof sendLog !== 'function'){
    sendLog = null;
}

// kshf namespace
var kshf = {
    surrogateCtor: function() {},
    // http://stackoverflow.com/questions/4152931/javascript-inheritance-call-super-constructor-or-use-prototype-chain
    extendClass: function(base, sub) {
      // Copy the prototype from the base to setup inheritance
      this.surrogateCtor.prototype = base.prototype;
      // Tricky huh?
      sub.prototype = new this.surrogateCtor();
      // Remember the constructor property was set wrong, let's fix it
      sub.prototype.constructor = sub;
    },
    summaryCount: 0,
    maxVisibleItems_Default: 100,
    scrollWidth: 19,
    previewTimeoutMS: 250,
    dt: {},
    dt_id: {},
    lang: {
        en: {
            ModifyBrowser: "Modify browser",
            OpenDataSource: "Open data source",
            ShowInfoCredits: "Show info &amp; credits",
            ShowFullscreen: "Fullscreen",
            RemoveFilter: "Remove filter",
            RemoveAllFilters: "Remove all filters",
            MinimizeSummary: "Close summary",
            OpenSummary: "Open summary",
            MaximizeSummary: "Maximize summary",
            RemoveSummary: "Remove summary",
            ReverseOrder: "Reverse order",
            Reorder: "Reorder",
            GetMoreInfo: "Get more info",
            Percentiles: "Percentiles",
            LockToCompare: "Lock to compare",
            Unlock: "Unlock",
            Search: "Search",
            CreatingBrowser: "Creating browser",
            Rows: "Rows",
            More: "More",
            LoadingData: "Loading data sources",
            ShowAll: "All",
            ScrollToTop: "Top",
            Absolute: "Absolute",
            Percent: "Percent",
            Relative: "Relative",
            Width: "Length",
            DragToFilter: "Drag to filter",
            And: "And",
            Or: "Or",
            Not: "Not",
            EditTitle: "Edit",
            ResizeBrowser: "Resize Browser",
            RemoveRecords: "Remove Record View"
        },
        tr: {
            ModifyBrowser: "Tarayıcıyı düzenle",
            OpenDataSource: "Veri kaynağını aç",
            ShowInfoCredits: "Bilgi",
            ShowFullscreen: "Tam ekran",
            RemoveFilter: "Filtreyi kaldır",
            RemoveAllFilters: "Tüm filtreleri kaldır",
            MinimizeSummary: "Özeti ufalt",
            OpenSummary: "Özeti aç",
            MaximizeSummary: "Özeti büyüt",
            RemoveSummary: "Özeti kaldır",
            ReverseOrder: "Ters sırala",
            Reorder: "Yeniden sırala",
            GetMoreInfo: "Daha fazla bilgi",
            Percentiles: "Yüzdeler",
            LockToCompare: "Kilitle ve karşılaştır",
            Unlock: "Kilidi kaldır",
            Search: "Ara",
            LoadingData: "Veriler yükleniyor...",
            CreatingBrowser: "Arayüz oluşturuluyor...",
            Rows: "Satır",
            More: "Daha",
            ShowAll: "Tüm",
            ScrollToTop: "Yukarı",
            Absolute: "Net",
            Percent: "Yüzde",
            Relative: "Görece",
            Width: "Genişlik",
            DragToFilter: "Sürükle ve filtre",
            And: "Ve",
            Or: "Veya",
            Not: "Değil",
            EditTitle: "Değiştir",
            ResizeBrowser: "Boyutlandır",
            RemoveRecords: "Kayıtları kaldır"
        },
        fr: {
            ModifyBrowser: "Modifier le navigateur",
            OpenDataSource: "Ouvrir la source de données",
            ShowInfoCredits: "Afficher les credits",
            RemoveFilter: "Supprimer le filtre",
            RemoveAllFilters: "Supprimer tous les filtres",
            MinimizeSummary: "Réduire le sommaire",
            OpenSummary: "Ouvrir le sommaire",
            MaximizeSummary: "Agrandir le sommaire",
            RemoveSummary: "??",
            ReverseOrder: "Inverser l'ordre",
            Reorder: "Réorganiser",
            GetMoreInfo: "Plus d'informations",
            Percentiles: "Percentiles",
            LockToCompare: "Bloquer pour comparer",
            Unlock: "Débloquer",
            Search: "Rechercher",
            CreatingBrowser: "Création du navigateur",
            Rows: "Lignes",
            More: "Plus",
            LoadingData: "Chargement des données",
            ShowAll: "Supprimer les filtres",
            ScrollToTop: "Début",
            Absolute: "Absolue",
            Percent: "Pourcentage",
            Relative: "Relative",
            Width: "Largeur",
            DragToFilter: "??",
            And: "??",
            Or: "??",
            Not: "??",
        },
        es: {
            ModifyBrowser: "Modificar navegador",
            OpenDataSource: "Abrir fuente de datos",
            ShowInfoCredits: "Mostrar información y créditos",
            ShowFullscreen: "Pantalla completa",
            RemoveFilter: "Eliminar filtro",
            RemoveAllFilters: "Eliminar todos los filtros",
            MinimizeSummary: "Cerrar resumen",
            OpenSummary: "Abrir resumen",
            MaximizeSummary: "Maximizar resumen",
            RemoveSummary: "Eliminar resumen",
            ReverseOrder: "Invertir orden",
            Reorder: "Reordenar",
            GetMoreInfo: "Obtener más información",
            Percentiles: "Percentiles",
            LockToCompare: "Bloquear para comparar",
            Unlock: "Desbloquear",
            Search: "Buscar",
            CreatingBrowser: "Creando explorador",
            Rows: "Filas",
            More: "Más",
            LoadingData: "Cargando fuentes de datos",
            ShowAll: "Todos",
            ScrollToTop: "Superior",
            Absolute: "Absoluto",
            Percent: "Porcentaje",
            Relative: "Relativo",
            Width: "Longitud",
            DragToFilter: "Arrastrar para filtrar",
            And: "Y",
            Or: "O",
            Not: "No",
            EditTitle: "Editar",
            ResizeBrowser: "Ajustar tamño del explorador",
            RemoveRecords: "Eliminar registros"
        },        
        cur: null // Will be set to en if not defined before a browser is loaded
    },

    LOG: {
        // Note: id parameter is integer alwats, info is string
        CONFIG                 : 1,
        // Filtering state
        // param: resultCt, selected(selected # of attribs, sep by x), filtered(filtered filter ids)
        FILTER_ADD             : 10,
        FILTER_CLEAR           : 11,
        // Filtering extra information, send in addition to filtering state messages above
        FILTER_CLEAR_ALL       : 12, // param: -
        FILTER_ATTR_ADD_AND    : 13, // param: id (filterID), info (attribID)
        FILTER_ATTR_ADD_OR     : 14, // param: id (filterID), info (attribID)
        FILTER_ATTR_ADD_ONE    : 15,
        FILTER_ATTR_ADD_OR_ALL : 16, // param: id (filterID)
        FILTER_ATTR_ADD_NOT    : 17, // param: id (filterID), info (attribID)
        FILTER_ATTR_EXACT      : 18, // param: id (filterID), info (attribID)
        FILTER_ATTR_UNSELECT   : 19, // param: id (filterID), info (attribID)
        FILTER_TEXTSEARCH      : 20, // param: id (filterID), info (query text)
        FILTER_INTRVL_HANDLE   : 21, // param: id (filterID) (TODO: Include range)
        FILTER_INTRVL_BIN      : 22, // param: id (filterID)
        FILTER_CLEAR_X         : 23, // param: id (filterID)
        FILTER_CLEAR_CRUMB     : 24, // param: id (filterID)
        FILTER_PREVIEW         : 25, // param: id (filterID), info (attribID for cat, histogram range (AxB) for interval)
        // Facet specific non-filtering interactions
        FACET_COLLAPSE         : 40, // param: id (facetID)
        FACET_SHOW             : 41, // param: id (facetID)
        FACET_SORT             : 42, // param: id (facetID), info (sortID)
        FACET_SCROLL_TOP       : 43, // param: id (facetID)
        FACET_SCROLL_MORE      : 44, // param: id (facetID)
        // List specific interactions
        LIST_SORT              : 50, // param: info (sortID)
        LIST_SCROLL_TOP        : 51, // param: -
        LIST_SHOWMORE          : 52, // param: info (itemCount)
        LIST_SORT_INV          : 53, // param: -
        // Item specific interactions
        ITEM_DETAIL_ON         : 60, // param: info (itemID)
        ITEM_DETAIL_OFF        : 61, // param: info (itemID)
        // Generic interactions
        DATASOURCE             : 70, // param: -
        INFOBOX                : 71, // param: -
        CLOSEPAGE              : 72, // param: -
        BARCHARTWIDTH          : 73, // param: info (width)
        RESIZE                 : 74, // param: -
    },
    Util: {
        sortFunc_List_String: function(a, b){
            return a.localeCompare(b);
        },
        sortFunc_List_Date: function(a, b){
            if(a===null) return -1;
            if(b===null) return 1;
            return a.getTime() - b.getTime();
        },
        sortFunc_List_Number: function(a, b){
            return b - a;
        },
        /** Given a list of columns which hold multiple IDs, breaks them into an array */
        cellToArray: function(dt, columns, splitExpr){
            if(splitExpr===undefined){
                splitExpr = /\b\s+/;
            }
            var j;
            dt.forEach(function(p){
                p = p.data;
                columns.forEach(function(column){
                    var list = p[column];
                    if(list===null) return;
                    if(typeof list==="number") {
                        p[column] = ""+list;
                        return;
                    }
                    var list2 = list.split(splitExpr);
                    list = [];
                    // remove empty "" items
                    for(j=0; j<list2.length; j++){
                        list2[j] = list2[j].trim();
                        if(list2[j]!=="") list.push(list2[j]);
                    }
                    p[column] = list;
                });
            });
        },
        /** You should only display at most 3 digits + k/m/etc */
        formatForItemCount: function(n){
            if(n<1000) {
                return n;
            }
            if(n<1000000) {
                // 1,000-999,999
                var thousands=n/1000;
                if(thousands<10){
                    return (Math.floor(n/100)/10)+"k";
                }
                return Math.floor(thousands)+"k";
            }
            if(n<1000000000) return Math.floor(n/1000000)+"m";
            return n;
        },
        nearestYear: function(d){
            var dr = new Date(Date.UTC(d.getUTCFullYear(),0,1));
            if(d.getUTCMonth()>6) dr.setUTCFullYear(dr.getUTCFullYear()+1);
            return dr;
        },
        nearestMonth: function(d){
            var dr = new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),1));
            if(d.getUTCDate()>15) dr.setUTCMonth(dr.getUTCMonth()+1);
            return dr;
        },
        nearestDay: function(d){
            var dr = new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth(),d.getUTCDate()));
            if(d.getUTCHours()>12) dr.setUTCDate(dr.getUTCDate()+1);
            return dr;
        },
        nearestHour: function(d){
        },
        nearestMinute: function(d){
        },
        clearArray: function(arr){
            while (arr.length > 0) {
              arr.pop();
            }
        },
        ignoreScrollEvents: false,
        scrollToPos_do: function(scrollDom, targetPos){
            kshf.Util.ignoreScrollEvents = true;
            // scroll to top
            var startTime = null;
            var scrollInit = scrollDom.scrollTop;
            var easeFunc = d3.ease('cubic-in-out');
            var scrollTime = 500;
            var animateToTop = function(timestamp){
                var progress;
                if(startTime===null) startTime = timestamp;
                // complete animation in 500 ms
                progress = (timestamp - startTime)/scrollTime;
                var m=easeFunc(progress);
                scrollDom.scrollTop = (1-m)*scrollInit+m*targetPos;
                if(scrollDom.scrollTop!==targetPos){
                    window.requestAnimationFrame(animateToTop);
                } else {
                    kshf.Util.ignoreScrollEvents = false;
                }
            };
            window.requestAnimationFrame(animateToTop);
        },
        toProperCase: function(str){
            return str.toLowerCase().replace(/\b[a-z]/g,function(f){return f.toUpperCase()});
        },
        setTransform: function(dom,transform){
            dom.style.webkitTransform = transform;
            dom.style.MozTransform = transform;
            dom.style.msTransform = transform;
            dom.style.OTransform = transform;
            dom.style.transform = transform;
        },
        // http://stackoverflow.com/questions/13627308/add-st-nd-rd-and-th-ordinal-suffix-to-a-number
        ordinal_suffix_of: function(i) {
            var j = i % 10,
                k = i % 100;
            if (j == 1 && k != 11) {
                return i + "st";
            }
            if (j == 2 && k != 12) {
                return i + "nd";
            }
            if (j == 3 && k != 13) {
                return i + "rd";
            }
            return i + "th";
        },
    },
    style: {
        color_chart_background_highlight: "rgb(194, 146, 124)"
    },
    fontLoaded: false,
    loadFont: function(){
        if(this.fontLoaded===true) return;
        WebFontConfig = {
            google: { families: [ 'Roboto:400,500,300,100,700:latin' ] }
        };
        var wf = document.createElement('script');
        wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
            '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
        wf.type = 'text/javascript';
        wf.async = 'true';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(wf, s);
        this.fontLoaded = true;
    }
};

// tipsy, facebook style tooltips for jquery
// Modified / simplified version for internal Keshif use
// version 1.0.0a
// (c) 2008-2010 jason frame [jason@onehackoranother.com]
// released under the MIT license
var activeTipsy = undefined;

function Tipsy(element, options) {
    this.jq_element = $(element);
    this.options = $.extend({}, this.defaults, options);
};
Tipsy.prototype = {
    defaults: {
        className: null,
        delayOut: 0,
        fade: true,
        fallback: '',
        gravity: 'n',
        offset: 0,
        offset_x: 0,
        offset_y: 0,
        opacity: 1
    },
    show: function() {
        var maybeCall = function(thing, ctx) {
            return (typeof thing == 'function') ? (thing.call(ctx)) : thing;
        };
        if(activeTipsy) {
            activeTipsy.hide();
        }

        activeTipsy=this;

        var title = this.getTitle();
        if(!title) return;
        var jq_tip = this.tip();

        jq_tip.find('.tipsy-inner')['html'](title);
        jq_tip[0].className = 'tipsy'; // reset classname in case of dynamic gravity
        jq_tip.remove().css({top: 0, left: 0, visibility: 'hidden', display: 'block'}).prependTo(document.body);

        var pos = $.extend({}, this.jq_element.offset(), {
            width: this.jq_element[0].offsetWidth,
            height: this.jq_element[0].offsetHeight
        });

        var actualWidth = jq_tip[0].offsetWidth,
            actualHeight = jq_tip[0].offsetHeight,
            gravity = maybeCall(this.options.gravity, this.jq_element[0]);

        var tp;
        switch (gravity.charAt(0)) {
            case 'n':
                tp = {top: pos.top + pos.height + this.options.offset, left: pos.left + pos.width / 2 - actualWidth / 2};
                break;
            case 's':
                tp = {top: pos.top - actualHeight - this.options.offset, left: pos.left + pos.width / 2 - actualWidth / 2};
                break;
            case 'e':
                tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left - actualWidth - this.options.offset};
                break;
            case 'w':
                tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left + pos.width + this.options.offset};
                break;
        }
        tp.top+=this.options.offset_y;
        tp.left+=this.options.offset_x;

        if (gravity.length == 2) {
            if (gravity.charAt(1) == 'w') {
                tp.left = pos.left + pos.width / 2 - 15;
            } else {
                tp.left = pos.left + pos.width / 2 - actualWidth + 15;
            }
        }

        jq_tip.css(tp).addClass('tipsy-' + gravity);
        jq_tip.find('.tipsy-arrow')[0].className = 'tipsy-arrow tipsy-arrow-' + gravity.charAt(0);
        if (this.options.className) {
            jq_tip.addClass(maybeCall(this.options.className, this.jq_element[0]));
        }

        if (this.options.fade) {
            jq_tip.stop().css({opacity: 0, display: 'block', visibility: 'visible'}).animate({opacity: this.options.opacity},200);
        } else {
            jq_tip.css({visibility: 'visible', opacity: this.options.opacity});
        }
    },
    hide: function(){
        activeTipsy = undefined;
        if (this.options.fade) {
            this.tip().stop().fadeOut(200,function() { $(this).remove(); });
        } else {
            this.tip().remove();
        }
    },
    getTitle: function() {
        var title, jq_e = this.jq_element, o = this.options;
        var title, o = this.options;
        if (typeof o.title == 'string') {
            title = jq_e.attr(o.title == 'title' ? 'original-title' : o.title);
        } else if (typeof o.title == 'function') {
            title = o.title.call(jq_e[0]);
        }
        title = ('' + title).replace(/(^\s*|\s*$)/, "");
        return title || o.fallback;
    },
    tip: function() {
        if(this.jq_tip) return this.jq_tip;
        this.jq_tip = $('<div class="tipsy"></div>').html('<div class="tipsy-arrow"></div><div class="tipsy-inner"></div>');
        this.jq_tip;
        this.jq_tip.data('tipsy-pointee', this.jq_element[0]);
        return this.jq_tip;
    },
};

/**
 * @constructor
 */
kshf.Item = function(d, idIndex){
    // the main data within item
    this.data = d;
    this.idIndex = idIndex; // TODO: Items don't need to have ID index, only one per table is enough??
    // Selection state
    //  1: selected for inclusion (AND)
    //  2: selected for inclusion (OR)
    // -1: selected for removal (NOT query)
    //  0: not selected
    this.selected = 0;
    // Items which are mapped/related to this item
    this.items = [];

    // By default, each item is aggregated as 1
    // You can modify this with a non-negative value
    // Note that the aggregation currently works by summation only.
    this.aggregate_Self = 1;

    this.aggregate_Active = 0;  // Active aggregate value
    this.aggregate_Preview = 0; // Previewed aggregate value
    this.aggregate_Total = 0;   // Total aggregate value

    // If true, filter/wanted state is dirty and needs to be updated.
    this._filterCacheIsDirty = true;
    // Cacheing filter state per eact facet in the system
    this.filterCache = [];
    // Wanted item / not filtered out
    this.isWanted = true;
    // Used by listDisplay to adjust animations. Only used by primary entity type for now.
    this.visibleOrder = 0;
    this.visibleOrder_pre = -1;
    // The data that's used for mapping this item, used as a cache.
    // This is accessed by filterID
    // Through this, you can also reach mapped DOM items
        // DOM elements that this item is mapped to
        // - If this is a paper, it can be paper type. If this is author, it can be author affiliation.
    this.mappedDataCache = []; // caching the values this item was mapped to
    // If true, item is currently selected to be included in link computation
    this.selectedForLink = false;

    this.DOM = {};
    // If item is primary type, this will be set
    this.DOM.record = undefined;
    // If item is used as a filter (can be primary if looking at links), this will be set
    this.DOM.facet  = undefined;
    // If true, updatePreview has propogated changes above
    this.updatePreview_Cache = false;
};
kshf.Item.prototype = {
    /** Returns unique ID of the item. */
    id: function(){
        return this.data[this.idIndex];
    },
    /** -- */
    setFilterCache: function(index,v){
        if(this.filterCache[index]===v) return;
        this.filterCache[index] = v;
        this._filterCacheIsDirty = true;
    },

    /** -- */
    f_selected: function(){ return this.selected!==0; },
    f_included: function(){ return this.selected>0; },

    is_NONE:function(){ return this.selected===0; },
    is_NOT: function(){ return this.selected===-1; },
    is_AND: function(){ return this.selected===1; },
    is_OR : function(){ return this.selected===2; },

    set_NONE: function(){
        if(this.inList!==undefined) {
            this.inList.splice(this.inList.indexOf(this),1);
        }
        this.inList = undefined;
        this.selected = 0; this.refreshFacetDOMSelected();
    },
    set_NOT: function(l){
        if(this.is_NOT()) return;
        this._insertToList(l);
        this.selected =-1; this.refreshFacetDOMSelected();
    },
    set_AND: function(l){
        if(this.is_AND()) return;
        this._insertToList(l);
        this.selected = 1; this.refreshFacetDOMSelected();
    },
    set_OR: function(l){
        if(this.is_OR()) return;
        this._insertToList(l);
        this.selected = 2; this.refreshFacetDOMSelected();
    },

    _insertToList: function(l){
        if(this.inList!==undefined) {
            this.inList.splice(this.inList.indexOf(this),1);
        }
        this.inList = l;
        l.push(this);
    },

    refreshFacetDOMSelected: function(){
        if(this.DOM.facet) this.DOM.facet.setAttribute("selected",this.selected);
    },

    /** -- */
    addItem: function(item){
        this.items.push(item);
        this.aggregate_Total+=item.aggregate_Self;
        this.aggregate_Active+=item.aggregate_Self;
    },
    /**
     * Updates isWanted state, and notifies all related filter attributes of the change.
     * With recursive parameter, you avoid updating status under facet passed in as recursive
     */
    updateWanted: function(recursive){
        if(!this._filterCacheIsDirty) return false;

        var me=this;
        var oldWanted = this.isWanted;

        // Checks if all filter results are true. At first "false", breaks the loop
        this.isWanted=true;
        this.filterCache.every(function(f){
            me.isWanted=me.isWanted&&f;
            return me.isWanted;
        });

        if(this.isWanted===true && oldWanted===false){
            // wanted now
            this.mappedDataCache.forEach(function(m){
                if(m===null) return;
                if(m.h){ // interval
                    if(m.b) m.b.aggregate_Active+=this.aggregate_Self;
                } else { // categorical
                    m.forEach(function(attrib){
                        var oldVal = attrib.aggregate_Active;
                        attrib.aggregate_Active+=this.aggregate_Self;
                        if(oldVal===0 && attrib.facet){
                            if(attrib.facet!==recursive && !attrib.facet.isLinked){
                                // it is now selected, see other DOM items it has and increment their count too
                                attrib.mappedDataCache.forEach(function(m){
                                    if(m===null) return;
                                    if(m.h) { // interval
                                        if(m.b) m.b.aggregate_Active+=attrib.aggregate_Self;
                                    } else { // categorical
                                        m.forEach(function(item){
                                            item.aggregate_Active+=attrib.aggregate_Self;
                                        });
                                    }
                                });
                            }
                        }
                    },this);
                }
            },this);
        } else if(this.isWanted===false && oldWanted===true){
            // unwanted now
            this.mappedDataCache.forEach(function(m){
                if(m===null) return;
                if(m.h){ // interval
                    if(m.b) m.b.aggregate_Active-=this.aggregate_Self;
                } else { // categorical
                    m.forEach(function(attrib){
                        attrib.aggregate_Active-=this.aggregate_Self;
                        if(attrib.aggregate_Active===0 && attrib.facet){
                            if(attrib.facet!==recursive && !attrib.facet.isLinked){
                                // it is now not selected. see other DOM items it has and decrement their count too
                                attrib.mappedDataCache.forEach(function(m){
                                    if(m===null) return;
                                    if(m.h) { // interval
                                        if(m.b) m.b.aggregate_Active-=attrib.aggregate_Self;
                                    } else { // categorical
                                        m.forEach(function(item){
                                            item.aggregate_Active-=attrib.aggregate_Self;
                                        });
                                    }
                                });
                            }
                        }
                    },this);
                }
            },this);
        }

        this._filterCacheIsDirty = false;
        return this.isWanted !== oldWanted;
    },
    /** Only updates wanted state if it is currently not wanted (resulting in More wanted items) */
    updateWanted_More: function(recursive){
        if(this.isWanted) return false;
        return this.updateWanted(recursive);
    },
    /** Only updates wanted state if it is currently wanted (resulting in Less wanted items) */
    updateWanted_Less: function(recursive){
        if(!this.isWanted) return false;
        return this.updateWanted(recursive);
    },
    updatePreview: function(parentFacet){
        if(!this.isWanted) return;

        if(this.updatePreview_Cache===false){
            this.updatePreview_Cache = true;
        } else {
            return;
        }

        if(this.DOM.record) this.DOM.record.setAttribute("highlight",true);

        // This is where you pass highlight information to through parent facet (which is primary entity)
        // if this item appears in a facet, it means it's used as a filter itself, propogate above
        if(this.facet && this.facet===parentFacet){
            // If this is the main item type, don't!
            // If this has no active item count, don't!
            if(!this.facet.isLinked && this.aggregate_Active>0){
                // see the main items stored under this one...
                this.items.forEach(function(item){ item.updatePreview(this.facet); },this);
            }
        }

        if(parentFacet && this.facet && this.aggregate_Preview===0) return;
        this.mappedDataCache.forEach(function(m){
            if(m===null) return;
            if(m.h) {
                if(m.b && m.b.aggregate_Active>0) m.b.aggregate_Preview+=this.aggregate_Self;
            } else {
                // if you are a sub-filter, go over the l
                m.forEach(function(item){
                    item.aggregate_Preview+=this.aggregate_Self;
                    if(item.aggregate_Preview===1 && item.facet){
                        if(!item.facet.isLinked && item.facet!==parentFacet){
                            // TODO: Don't go under the current one, if any
                            item.updatePreview(parentFacet);
                        }
                    }
                },this);
            }
        },this);
    },
    /**
     * Called on mouse-over on a primary item type, then recursively on all summaries and their sub-summaries
     * Higlights all relevant UI parts to this UI item
     */
    highlightAll: function(recurse){
        if(this.DOM.record) this.DOM.record.setAttribute("highlight",recurse?"selected":true);
        if(this.DOM.facet)  this.DOM.facet.setAttribute("highlight",recurse?"selected":true);
        if(this.cliqueRow)  this.cliqueRow.setAttribute("highlight","selected");

        if(this.DOM.record && !recurse) return;
        this.mappedDataCache.forEach(function(d){
            if(d===null) return; // no mapping for this index
            if(d.h){ // interval facet
                d.h.setSelectedPosition(d.v);
            } else { // categorical facet
                d.forEach(function(item){
                    // skip going through main items that contain a link TO this item
                    if(this.DOM.record && item.DOM.record)
                        return;
                    item.highlightAll(false);
                },this);
            }
        },this);
    },
    /** Removes higlight from all relevant UI parts to this UI item */
    nohighlightAll: function(recurse){
        if(this.DOM.record) this.DOM.record.setAttribute("highlight",false);
        if(this.DOM.facet)  this.DOM.facet .setAttribute("highlight",false);
        if(this.cliqueRow)   this.cliqueRow.setAttribute("highlight",false);

        if(this.DOM.record && !recurse) return;
        this.mappedDataCache.forEach(function(d,i){
            if(d===null) return; // no mapping for this index
            if(d.h){ // interval facet
                d.h.hideSelectedPosition(d.v);
            } else { // categorical facet
                d.forEach(function(item){
                    // skip going through main items that contain a link TO this item
                    if(this.DOM.record && item.DOM.record) return;
                    item.nohighlightAll(false);
                },this);
            }
        },this);
    },
    setSelectedForLink: function(v){
        this.selectedForLink = v;
        if(this.DOM.record){
            this.DOM.record.setAttribute("selectedForLink",v);
        }
        if(v===false){
            this.set_NONE();
        }
    }
};

kshf.Filter = function(id, opts){
    this.isFiltered = false;

    this.browser = opts.browser;
    this.parentSummary = opts.parentSummary;

    this.onClear = opts.onClear;
    this.onFilter = opts.onFilter;
    this.hideCrumb = opts.hideCrumb || false;
    this.filterView_Detail = opts.filterView_Detail; // must be a function
    this.filterHeader = opts.filterHeader;

    this.id = id;
    this.parentSummary.items.forEach(function(item){
        item.setFilterCache(this.id,true);
    },this);
    this.how = "All";
    this.filterSummaryBlock = null;
};
kshf.Filter.prototype = {
    addFilter: function(forceUpdate,recursive){
        var parentFacet=this.parentSummary.parentFacet;
        this.isFiltered = true;

        if(this.onFilter) this.onFilter.call(this,this.parentSummary);

        var stateChanged = false;
        if(recursive===undefined) recursive=true;

        var how=0;
        if(this.how==="LessResults") how = -1;
        if(this.how==="MoreResults") how = 1;

        this.parentSummary.items.forEach(function(item){
            // if you will show LESS results and item is not wanted, skip
            // if you will show MORE results and item is wanted, skip
            if(!(how<0 && !item.isWanted) && !(how>0 && item.isWanted)){
                var changed = item.updateWanted(recursive);
                stateChanged = stateChanged || changed;
            }
            if(parentFacet && parentFacet.hasCategories()){
                if(item.isWanted)
                    item.set_OR(parentFacet.summaryFilter.selected_OR);
                else
                    item.set_NONE();
            }
        },this);

        // if this has a parent facet (multi-level), link selection from this to the parent facet
        if(parentFacet && parentFacet.hasCategories()){
            parentFacet.updateCatCount_Wanted();
            parentFacet.summaryFilter.how = "All";
            // re-run the parents attribute filter...
            parentFacet.summaryFilter.linkFilterSummary = "";
            parentFacet.summaryFilter.addFilter(false,parentFacet); // This filter will update the browser later if forceUpdate===true
            parentFacet._update_Selected();
        }

        this._refreshFilterSummary();

        if(forceUpdate===true){
            this.browser.update_itemsWantedCount();
            this.browser.refresh_filterClearAll();
            if(stateChanged) this.browser.updateAfterFilter(-1);
            if(sendLog) sendLog(kshf.LOG.FILTER_ADD,this.browser.getFilterState());
        }
    },
    clearFilter: function(forceUpdate,recursive, updateWanted){
        if(!this.isFiltered) return;
        var parentFacet=this.parentSummary.parentFacet;
        var hasEntityParent = false;
        if(this.parentSummary.hasEntityParent)
            hasEntityParent = this.parentSummary.hasEntityParent();

        this.isFiltered = false;

        // clear filter cache - no other logic is necessary
        this.parentSummary.items.forEach(function(item){ item.setFilterCache(this.id,true); },this);

        if(recursive===undefined) recursive=true;

        if(updateWanted!==false){
            this.parentSummary.items.forEach(function(item){
                if(!item.isWanted){
                    item.updateWanted(recursive);
                }
                if(parentFacet && parentFacet.hasCategories()){
                    if(item.isWanted)
                        item.set_OR(parentFacet.summaryFilter.selected_OR);
                    else
                        item.set_NONE();
                }
            });
        }

        this._refreshFilterSummary();

        if(this.onClear) this.onClear.call(this,this.parentSummary);

        if(forceUpdate!==false){
            if(hasEntityParent){
                parentFacet.updateCatCount_Wanted();
                parentFacet.summaryFilter.how = "All";
                if(parentFacet.catCount_Wanted===parentFacet.catCount_Total){
                    parentFacet.summaryFilter.clearFilter(false,parentFacet); // force update
                } else {
                    // re-run the parents attribute filter...
                    parentFacet.summaryFilter.linkFilterSummary = "";
                    parentFacet.summaryFilter.addFilter(false,parentFacet); // force update
                }
            }

            if(this.parentSummary.subFacets){
                this.parentSummary.subFacets.forEach(function(summary){
                    summary.summaryFilter.clearFilter(false,false,false);
                });
                // if this has sub-facets, it means this also maintains an isWanted state.
                // Sub facets are cleared, but the attribs isWanted state is NOT updated
                // Fix that, now.
                if(this.parentSummary.subFacets.length>0){
                    this.parentSummary._cats.forEach(function(item){
                        item.isWanted = true;
                        item._filterCacheIsDirty = false;
                    });
                }
            }

            this.browser.update_itemsWantedCount();
            this.browser.refresh_filterClearAll();
            this.browser.updateAfterFilter(1); // more results

            if(sendLog) {
                sendLog(kshf.LOG.FILTER_CLEAR,this.browser.getFilterState());
            }
        }
    },

    /** Don't call this directly */
    _refreshFilterSummary: function(){
        if(this.hideCrumb===true) return;
        if(!this.isFiltered){
            var root = this.filterSummaryBlock;
            if(root===null || root===undefined) return;
            root.attr("ready",false);
            setTimeout(function(){ root[0][0].parentNode.removeChild(root[0][0]); }, 350);
            this.filterSummaryBlock = null;
        } else {
            // insert DOM
            if(this.filterSummaryBlock===null) {
                this.filterSummaryBlock = this.insertFilterSummaryBlock();
                if(this.filterSummaryBlock===false){
                    this.filterSummaryBlock=null;
                    return;
                }
            }
            if(this.parentSummary!==undefined) this.filterHeader = this.parentSummary.summaryTitle;
            this.filterSummaryBlock.select(".filterHeader").html(this.filterHeader);
            this.filterSummaryBlock.select(".filterDetails").html(this.filterView_Detail.call(this, this.parentSummary));
        }
    },
    /** Inserts a summary block to the list breadcrumb DOM */
    /** Don't call this directly */
    insertFilterSummaryBlock: function(){
        var x;
        var me=this;
        if(this.browser.DOM.filtercrumbs===undefined) return false;
        x = this.browser.DOM.filtercrumbs
            .append("span").attr("class","filter-block")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: 'n',
                    title: function(){ return kshf.lang.cur.RemoveFilter; }
                })
            })
            .on("mouseenter",function(){
                this.tipsy.show();
                d3.event.stopPropagation();
            })
            .on("mouseleave",function(){
                this.tipsy.hide();
                d3.event.stopPropagation();
            })
            .on("click",function(){
                this.tipsy.hide();
                me.clearFilter();
                // delay layout height update
                setTimeout( function(){ me.browser.updateLayout_Height();}, 1000);
                if(sendLog) sendLog(kshf.LOG.FILTER_CLEAR_CRUMB, {id: this.id});
            })
            ;
        x.append("span").attr("class","chartClearFilterButton summary")
            .append("span").attr("class","fa fa-times")
            ;
        var y = x.append("span").attr("class","sdsdsds");
        y.append("span").attr("class","filterHeader");
        y.append("span").attr("class","filterDetails");
        // animate appear
        window.getComputedStyle(x[0][0]).opacity;
        x.attr("ready",true);
        return x;
    }
};

/**
 * The list UI
 * @constructor
 */
kshf.RecordDisplay = function(kshf_, config, root){
    var me = this;
    this.browser = kshf_;
    this.DOM = {};

    this.config = config;

    this.scrollTop_cache=0;

    this.linkColumnWidth = 85;
    this.linkColumnWidth_ItemCount = 25;
    this.linkColumnWidth_BarMax = this.linkColumnWidth-this.linkColumnWidth_ItemCount-3;
    this.selectColumnWidth = 17;

    this.items = this.browser.items;

    this.autoExpandMore = true;
    if(config.autoExpandMore===false) this.autoExpandMore = false;

    this.maxVisibleItems_Default = config.maxVisibleItems_Default || kshf.maxVisibleItems_Default;
    this.maxVisibleItems = this.maxVisibleItems_Default; // This is the dynamic property

    this.sortingOpts = config.sortingOpts || [ {title:this.browser.items[0].idIndex} ];
    if(!Array.isArray(this.sortingOpts)){
        this.sortingOpts = [this.sortingOpts];
    }
    this.prepSortingOpts();
    this.sortingOpt_Active = this.sortingOpts[0];

    this.displayType   = config.displayType   || 'list'; // 'grid', 'list'
    this.detailsToggle = config.detailsToggle || 'zoom'; // 'one', 'zoom', 'off' (any other string counts as off practically)
    this.linkText      = config.linkText      || "Related To";

    this.visibleCb = config.visibleCb;
    this.detailCb  = config.detailCb;

    this.showRank = config.showRank || false;

    this.textSearchSummary = null; // no text search summary by default
    this.recordViewSummary = null;

    this.DOM.root = root.select(".recordDisplay")
        .attr('detailsToggle',this.detailsToggle)
        .attr('displayType',this.displayType)
        .attr('showRank',this.showRank)
        .attr('hasRecordView',false);

    var zone=this.DOM.root.append("div").attr("class","dropZone dropZone_recordView")
        .on("mouseenter",function(){ this.setAttribute("readyToDrop",true);  })
        .on("mouseleave",function(){ this.setAttribute("readyToDrop",false); })
        .on("mouseup",function(event){
            var movedSummary = me.browser.movedSummary;
            if(movedSummary===null || movedSummary===undefined) return;

            movedSummary.refreshNuggetDisplay();

            me.setRecordViewSummary(movedSummary);

            me.updateVisibleIndex();
            me.updateItemVisibility(false,true);

            if(me.textSearchSummary===null) me.setTextSearchSummary(movedSummary);

            me.browser.updateLayout();
        });
    zone.append("div").attr("class","dropIcon fa fa-list-ul");
    
    this.DOM.recordViewHeader=this.DOM.root.append("div").attr("class","recordDisplay--Header");
    this.initDOM_RecordViewHeader();

    this.DOM.listItemGroup = this.DOM.root.append("div").attr("class","listItemGroup")
        .on("scroll",function(d){
            if(this.scrollHeight-this.scrollTop-this.offsetHeight<10){
                if(me.autoExpandMore===false){
                    me.DOM.showMore.attr("showMoreVisible",true);
                } else {
                    me.showMore(); // automatically add more records
                }
            } else{
                me.DOM.showMore.attr("showMoreVisible",false);
            }
            me.DOM.scrollToTop.style("visibility", this.scrollTop>0?"visible":"hidden");
            me.DOM.adjustSortColumnWidth.style("top",(this.scrollTop-2)+"px")
        });

    this.DOM.adjustSortColumnWidth = this.DOM.listItemGroup.append("div")
        .attr("class","adjustSortColumnWidth dragWidthHandle")
        .on("mousedown", function (d, i) {
            if(d3.event.which !== 1) return; // only respond to left-click
            root.style('cursor','ew-resize');
            var _this = this;
            var mouseDown_x = d3.mouse(document.body)[0];
            var mouseDown_width = me.sortColWidth;

            me.browser.DOM.pointerBlock.attr("active","");

            root.on("mousemove", function() {
                _this.setAttribute("dragging","");
                me.setSortColumnWidth(mouseDown_width+(d3.mouse(document.body)[0]-mouseDown_x));
            }).on("mouseup", function(){
                root.style('cursor','default');
                me.browser.DOM.pointerBlock.attr("active",null);
                root.on("mousemove", null).on("mouseup", null);
                _this.removeAttribute("dragging");
            });
            d3.event.preventDefault();
        });

    this.DOM.showMore = this.DOM.root.append("div").attr("class","showMore")
        .attr("showMoreVisible",false)
        .on("mouseenter",function(){ d3.select(this).selectAll(".loading_dots").attr("anim",true); })
        .on("mouseleave",function(){ d3.select(this).selectAll(".loading_dots").attr("anim",null); })
        .on("click",function(){ me.showMore(); })
        ;
        this.DOM.showMore.append("span").attr("class","MoreText").html("Show More");
        this.DOM.showMore.append("span").attr("class","Count CountAbove");
        this.DOM.showMore.append("span").attr("class","Count CountBelow");
        this.DOM.showMore.append("span").attr("class","loading_dots loading_dots_1");
        this.DOM.showMore.append("span").attr("class","loading_dots loading_dots_2");
        this.DOM.showMore.append("span").attr("class","loading_dots loading_dots_3");

    if(config.recordView!==undefined){
        if(typeof config.recordView === 'string'){
            this.setRecordViewSummary(this.browser.summaries_by_name[config.recordView]);
        }
        if(typeof config.recordView === 'function'){
            this.setRecordViewSummary(this.browser.createSummary('_RecordView_',config.recordView,'categorical'));
        }
    }

    if(config.textSearch){
        // Find the summary. If it is not there, create it
        if(typeof(config.textSearch)==="string"){
            this.setTextSearchSummary( this.browser.summaries_by_name[config.textSearch] );
        } else {
            var title = config.textSearch.title;
            var value = config.textSearch.value;
            if(title!==undefined){
                var summary = this.browser.summaries_by_name[config.textSearch];
                if(summary){
                    this.setTextSearchSummary(summary);
                } else {
                    if(typeof(value)==="function"){
                        this.setTextSearchSummary(browser.createSummary(title,value,'categorical'));
                    } else if(typeof(value)==="string"){
                        this.setTextSearchSummary(browser.changeSummaryName(value,title));
                    };
                }
            }
        }
    }
};

kshf.RecordDisplay.prototype = {
    /** -- */
    setDetailsToggle: function(v){
        this.detailsToggle = v;
        this.DOM.root.attr('detailsToggle',this.detailsToggle)
    },
    /** -- */
    initDOM_RecordViewHeader: function(){
        var me=this;
        this.DOM.recordViewHeader.append("div").attr("class","itemRank_control fa")
            .each(function(){
                this.tipsy = new Tipsy(this, {gravity: 'n', title: function(){ 
                    return (me.showRank?"Hide":"Show")+" ranking"; 
                }});
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("click",function(){
                me.setShowRank(!me.showRank);
                d3.event.preventDefault();
                d3.event.stopPropagation();
            });

        this.initDOM_SortSelect();
        this.initDOM_GlobalTextSearch();

        this.DOM.recordViewHeader.append("div").attr("class","buttonRecordViewRemove fa fa-times")
            .each(function(){
                this.tipsy = new Tipsy(this, {gravity: 'ne', title: function(){ return kshf.lang.cur.RemoveRecords; }});
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout", function(){ this.tipsy.hide(); })
            .on("click",function(){
                me.removeRecordViewSummary();
            });

        this.DOM.scrollToTop = this.DOM.recordViewHeader.append("div").attr("class","scrollToTop fa fa-arrow-up")
            .each(function(){
                this.tipsy = new Tipsy(this, {gravity: 'e', title: function(){ return kshf.lang.cur.ScrollToTop; }});
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout", function(){ this.tipsy.hide(); })
            .on("click",function(d){
                kshf.Util.scrollToPos_do(me.DOM.listItemGroup[0][0],0);
                if(sendLog) sendLog(kshf.LOG.LIST_SCROLL_TOP);
            });
    },
    /* -- */
    initDOM_GlobalTextSearch: function(){
        var me=this;

        this.textFilter = this.browser.createFilter({
            parentSummary: this.browser, 
            hideCrumb: true,
            onClear: function(){
                me.DOM.recordTextSearch.select(".clearText").style('display','none');
                me.DOM.recordTextSearch.select("input")[0][0].value = "";
            },
            onFilter: function(){
                me.DOM.recordTextSearch.select(".clearText").style('display','inline-block');

                var query = [];

                // split the input by " character
                var processed = this.filterStr.split('"');
                processed.forEach(function(block,i){
                    if(i%2===0) {
                        block.split(/\s+/).forEach(function(q){ query.push(q)});
                    } else {
                        query.push(block);
                    }
                });

                // Remove the empty strings
                query = query.filter(function(v){ return v!==""});

                // go over all the items in the list, search each keyword separately
                // If some search matches, return true (any function)
                var summaryFunc = me.textSearchSummary.summaryFunc;
                me.items.forEach(function(item){
                    var f = ! query.every(function(v_i){
                        var v = summaryFunc.call(item.data,item);
                        if(v===null || v===undefined) return true;
                        return (""+v).toLowerCase().indexOf(v_i)===-1;
                    });
                    item.setFilterCache(this.id,f);
                },this);
            },
        });

        this.DOM.recordTextSearch = this.DOM.recordViewHeader.append("span").attr("class","recordTextSearch");

        var x= this.DOM.recordTextSearch.append("div").attr("class","dropZone_textSearch")
            .on("mouseenter",function(){
                this.style.backgroundColor = "rgb(255, 188, 163)";
            })
            .on("mouseleave",function(){
                this.style.backgroundColor = "";
            })
            .on("mouseup",function(){
                me.setTextSearchSummary(me.movedSummary);
            });
        x.append("div").attr("class","dropZone_textSearch_text").text("Text search");

        this.DOM.recordTextSearch.append("i").attr("class","fa fa-search searchIcon");
        this.DOM.recordTextSearch.append("input").attr("class","mainTextSearch_input")
            .on("keydown",function(){
                var x = this;
                if(this.timer){
                    clearTimeout(this.timer);
                    this.timer = null;
                }
                this.timer = setTimeout( function(){
                    me.textFilter.filterStr = x.value.toLowerCase();
                    if(me.textFilter.filterStr!=="") {
                        me.textFilter.addFilter(true);
                    } else {
                        me.textFilter.clearFilter();
                    }
                    if(sendLog) sendLog(kshf.LOG.FILTER_TEXTSEARCH, {id: me.textFilter.id, info: me.textFilter.filterStr});
                    x.timer = null;
                }, 750);
            });
        this.DOM.recordTextSearch.append("i").attr("class","fa fa-times-circle clearText")
            .on("click",function() { me.textFilter.clearFilter(); });
    },
    /** -- */
    setRecordViewSummary: function(summary){
        if(summary===undefined || summary===null) return;
        if(this.recordViewSummary===summary) return;
        if(this.recordViewSummary){
            this.removeRecordViewSummary();
        }
        this.DOM.root.attr('hasRecordView',true);
        this.recordViewSummary = summary;
        this.recordViewSummary.isRecordView = true;
        this.recordViewSummary.refreshNuggetDisplay();

        this.sortRecords();
        this.insertRecords();
        this.setSortColumnWidth(this.config.sortColWidth || 50); // default: 50px;
        this.refreshRecordContent(this.DOM.recordsContent);
    },
    /** -- */
    removeRecordViewSummary: function(){
        if(this.recordViewSummary===null) return;
        this.DOM.root.attr("hasRecordView",false);
        this.recordViewSummary.isRecordView = false;
        this.recordViewSummary.refreshNuggetDisplay()
        this.recordViewSummary = null;
    },
    /** -- */
    setTextSearchSummary: function(summary){
        if(summary===undefined || summary===null) return;
        //if(this.textSearchSummary===summary) return;
        this.textSearchSummary = summary;
        this.textSearchSummary.isTextSearch = true;
        this.DOM.recordTextSearch
            .attr("isActive",true)
            .select("input").attr("placeholder", kshf.lang.cur.Search+": "+summary.summaryTitle);
    },
    /** -- */
    addSortingOption: function(summary){
        // If parameter summary is already a sorting option, nothing else to do
        if(this.sortingOpts.some(function(o){ return o===summary; })) return;

        this.sortingOpts.push(summary);

        summary.sortLabel   = summary.summaryFunc;
        summary.sortInverse = false;
        summary.sortFunc    = this.getSortFunc(summary.summaryFunc);

        this.prepSortingOpts();
        this.refreshSortingOptions();
        if(sendLog) sendLog(kshf.LOG.LIST_SORT, {info: this.selectedIndex});
    },
    /** -- */
    initDOM_SortSelect: function(){
        var me=this;

        this.DOM.header_listSortColumn = this.DOM.recordViewHeader.append("div")
            .attr("class","header_listSortColumn");
        var x=this.DOM.header_listSortColumn.append("div").attr("class","dropZone_resultSort")
            .on("mouseenter",function(){
                this.style.backgroundColor = "rgb(255, 188, 163)";
            })
            .on("mouseleave",function(event){
                this.style.backgroundColor = "";
            })
            .on("mouseup",function(event){
                me.addSortingOption(me.browser.movedSummary);
                me.setSortingOpt_Active(me.sortingOpts.length-1);
                me.DOM.listSortOptionSelect[0][0].selectedIndex = me.sortingOpts.length-1;
            })
            ;
        x.append("span").attr("class","dropZone_resultSort_text");

        this.DOM.listSortOptionSelect = this.DOM.header_listSortColumn.append("select")
            .attr("class","listSortOptionSelect")
            .on("change", function(){
                me.setSortingOpt_Active(this.selectedIndex);
                if(sendLog) sendLog(kshf.LOG.LIST_SORT, {info: this.selectedIndex});
            })
            ;

        this.refreshSortingOptions();

        this.DOM.removeSortOption = this.DOM.recordViewHeader
            .append("span").attr("class","removeSortOption_wrapper")
            .append("span").attr("class","removeSortOption fa")
            .each(function(){
                this.tipsy = new Tipsy(this, {gravity: 'n', title: function(){ return "Remove current sorting option"; }});
            })
            .style("display",(this.sortingOpts.length<2)?"none":"inline-block")
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout",function(d,i){ this.tipsy.hide(); })
            .on("click",function(){
                var index=-1;
                me.sortingOpts.forEach(function(o,i){ if(o===me.sortingOpt_Active) index=i; })
                if(index!==-1){
                    me.sortingOpts.splice(index,1);
                    if(index===me.sortingOpts.length) index--;
                    me.prepSortingOpts();
                    me.setSortingOpt_Active(index);
                    me.refreshSortingOptions();
                    me.DOM.listSortOptionSelect[0][0].selectedIndex = index;
                }
            })

        this.DOM.recordViewHeader.append("span").attr("class","sortColumn sortButton fa")
            .on("click",function(d){
                me.sortingOpt_Active.inverse = me.sortingOpt_Active.inverse?false:true;
                this.setAttribute("inverse",me.sortingOpt_Active.inverse);
                me.browser.items.reverse();
                me.DOM.listItems = me.DOM.listItemGroup.selectAll(".listItem")
                    .data(me.browser.items, function(d){ return d.id(); })
                    .order();
                me.updateVisibleIndex();
                me.updateItemVisibility(false,true);
                kshf.Util.scrollToPos_do(me.DOM.listItemGroup[0][0],0);
                if(sendLog) sendLog(kshf.LOG.LIST_SORT_INV);
            })
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){ return kshf.lang.cur.ReverseOrder; }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout",function(){ this.tipsy.hide(); });
    },
    /** -- */
    refreshRecordContent: function(d3_selection){
        var me=this;
        d3_selection.html(function(d){ return me.recordViewSummary.summaryFunc.call(d.data,d); });
    },
    /** -- */
    refreshRecordRanks: function(d3_selection){
        if(!this.showRank) return; // Do not refresh if not shown...
        d3_selection.text(function(d){
            if(d.visibleOrder<0) return "";
            return d.visibleOrder+1;
        });
    },
    /** -- */
    refreshRecordSortLabels: function(d3_selection){
        if(this.displayType!=="list") return;
        var labelFunc=this.sortingOpt_Active.sortLabel;
        var unitName =this.sortingOpt_Active.unitName;
        var sortColformat = d3.format(".s");
        if(this.sortingOpt_Active.hasTime){
            sortColformat = d3.time.format("%Y");
        }

        d3_selection.html(function(d){
            var s=labelFunc.call(d.data);
            if(s===null || s===undefined) return "";
            this.setAttribute("title",s);
            if(typeof s!=="string") s = sortColformat(s);
            if(unitName) s+="<span class='unitName'>"+unitName+"</span>";
            return s;
        });
    },
    /** -- */
    refreshSortingOptions: function(){
        this.DOM.listSortOptionSelect.selectAll("option").remove();
        this.DOM.listSortOptionSelect.selectAll("option").data(this.sortingOpts)
            .enter().append("option").html(function(summary){ return summary.summaryTitle; });
        this.DOM.listSortOptionSelect[0][0].value = this.sortingOpt_Active.summaryTitle;
    },
    /** -- */
    prepSortingOpts: function(){
        this.sortingOpts.forEach(function(sortOpt,i){
            if(sortOpt.summaryTitle) return; // It already points to a summary
            if(typeof(sortOpt)==="string"){
                sortOpt = { title: sortOpt };
            }

            var summary = this.browser.summaries_by_name[sortOpt.title];
            if(summary===undefined){
                if(typeof(sortOpt.value)==="string"){
                    summary = this.browser.changeSummaryName(sortOpt.value,sortOpt.title);
                } else{
                    summary = this.browser.createSummary(sortOpt.title,sortOpt.value, "interval");
                    if(sortOpt.unitName){
                        summary.setUnitName(sortOpt.unitName);
                    }
                }
            }

            summary.sortLabel   = sortOpt.label || summary.summaryFunc;
            summary.sortInverse = sortOpt.inverse  || false;
            summary.sortFunc    = sortOpt.sortFunc || this.getSortFunc(summary.summaryFunc);

            this.sortingOpts[i] = summary;
        },this);
        if(this.DOM.removeSortOption)
            this.DOM.removeSortOption.style("display",(this.sortingOpts.length<2)?"none":"inline-block");
    },
    /** -- */
    setSortingOpt_Active: function(index){
        if(index<0 || index>=this.sortingOpts.length) return;
        this.sortingOpt_Active = this.sortingOpts[index];

        this.sortRecords();
        this.DOM.listItems = this.DOM.listItemGroup.selectAll(".listItem")
            .data(this.browser.items, function(d){ return d.id(); })
            .order();

        this.updateVisibleIndex();
        this.updateItemVisibility();
        this.refreshRecordSortLabels(this.DOM.recordsSortCol);
        kshf.Util.scrollToPos_do(this.DOM.listItemGroup[0][0],0);
    },
    /** -- */
    setSortColumnWidth: function(v){
        if(this.displayType!=='list') return;
        this.sortColWidth = Math.max(Math.min(v,110),30);
        this.DOM.recordsSortCol.style("width",this.sortColWidth+"px")
        this.refreshAdjustSortColumnWidth();
    },
    /** -- */
    refreshAdjustSortColumnWidth: function(){
        this.DOM.adjustSortColumnWidth.style("left",
            (this.sortColWidth-2)+(this.showRank?15:0)+"px")
    },
    /** -- */
    setShowRank: function(v){
        this.showRank=v;
        this.DOM.root.attr('showRank',this.showRank);
        this.refreshRecordRanks(this.DOM.recordRanks);
        this.refreshAdjustSortColumnWidth();
    },
    /** Insert items into the UI, called once on load */
    insertRecords: function(){
        var me = this, x;

        var newRecords = this.DOM.listItemGroup.selectAll(".listItem")
            .data(this.browser.items, function(d){ return d.id(); })
        .enter()
            .append("div")
            .attr("class","listItem")
            .attr("details","false")
            .attr("highlight",false)
            .attr("animSt","visible")
            .attr("itemID",function(d){ return d.id(); }) // can be used to apply custom CSS
            // store the link to DOM in the data item
            .each(function(d){ d.DOM.record = this; })
            .on("mouseenter",function(d){
                d.highlightAll(true);
                d.items.forEach(function(item){ item.highlightAll(false); });
            })
            .on("mouseleave",function(d){
                this.setAttribute("highlight","false");
                d.nohighlightAll(true);
                d.items.forEach(function(item){ item.nohighlightAll(false); });
            });
        
        x = newRecords.append("span").attr("class","recordRank")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: 'e',
                    title: function(){ return kshf.Util.ordinal_suffix_of((d.visibleOrder+1)); }
                });
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseout"  ,function(){ this.tipsy.hide(); });
        this.refreshRecordRanks(x);

        if(this.displayType==='list'){
            x = newRecords.append("div").attr("class","recordSortCol");
            this.refreshRecordSortLabels(x);
        }

        newRecords.append("div").attr("class","recordToggleDetail")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity:'s',
                    title: function(){
                        if(me.detailsToggle==="one" && this.displayType==='list')
                            return d.showDetails===true?"Show less":"Show more";
                        return kshf.lang.cur.GetMoreInfo;
                    }
                });
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .append("span").attr("class","item_details_toggle fa")
                .on("click", function(d){
                    this.parentNode.tipsy.hide();
                    if(me.detailsToggle==="one" && me.displayType==='list'){
                        me.setRecordDetails(d,!d.showDetails);
                    }
                    if(me.detailsToggle==="zoom"){
                        me.browser.updateItemZoomText(d);
                        me.browser.panel_infobox.attr("show","itemZoom");
                    }
                });

        x = newRecords.append("div").attr("class","content");

        this.DOM.listItems      = this.DOM.listItemGroup.selectAll(".listItem");
        this.DOM.recordsSortCol = this.DOM.listItemGroup.selectAll(".recordSortCol");
        this.DOM.recordsContent = this.DOM.listItemGroup.selectAll(".content");
        this.DOM.recordRanks    = this.DOM.listItemGroup.selectAll(".recordRank");
    },
    /** -- */
    setRecordDetails: function(item, value){
        item.showDetails = value;
        item.DOM.record.setAttribute('details', item.showDetails);
        if(item.showDetails){
            if(this.detailCb) this.detailCb.call(item.data, item);
        }
        if(sendLog) sendLog(kshf.LOG.ITEM_DETAIL_OFF, {info:item.id(), value:value});
    },
    /** -- */
    showMore: function(){
        this.maxVisibleItems *= 2;
        this.updateItemVisibility(true);
        this.DOM.showMore.attr("showMoreVisible",false);
        if(sendLog) sendLog(kshf.LOG.LIST_SHOWMORE,{info: this.maxVisibleItems});
    },
    /** Sort all records given the active sort option
     *  Records are only sorted on init & when active sorting option changes.
     *  They are not resorted on filtering. ** Filtering does not affect record sorting.
     */
    sortRecords: function(){
        var sortValueFunc = this.sortingOpt_Active.summaryFunc;
        var sortFunc = this.sortingOpt_Active.sortFunc;
        var inverse = this.sortingOpt_Active.sortInverse;
        this.browser.items.sort(
            function(a,b){
                // Put filtered/remove data to later position
                // !! Don't do above!! Then, when you filter set, you'd need to re-order
                // Now, you don't need to re-order after filtering, which is a nice property to have.
                var v_a = sortValueFunc.call(a.data,a);
                var v_b = sortValueFunc.call(b.data,b);

                if(isNaN(v_a)) v_a = undefined;
                if(isNaN(v_b)) v_b = undefined;
                if(v_a===null) v_a = undefined;
                if(v_b===null) v_b = undefined;

                if(v_a===undefined && v_b!==undefined) return  1;
                if(v_b===undefined && v_a!==undefined) return -1;
                if(v_b===undefined && v_a===undefined) return 0;

                var dif=sortFunc(v_a,v_b);
                if(dif===0) dif=b.id()-a.id();
                if(inverse) return -dif;
                return dif; // use unique IDs to add sorting order as the last option
            }
        );
    },
    /** Returns the sort value type for given sort Value function */
    getSortFunc: function(sortValueFunc){
        // 0: string, 1: date, 2: others
        var sortValueFunction, same;

        // find appropriate sortvalue type
        for(var k=0, same=0; true ; k++){
            if(same===3 || k===this.browser.items.length){
                break;
            }
            var item = this.browser.items[k];
            var f = sortValueFunc.call(item.data,item);
            var sortValueType_temp2;
            switch(typeof f){
            case 'string': sortValueType_temp2 = kshf.Util.sortFunc_List_String; break;
            case 'number': sortValueType_temp2 = kshf.Util.sortFunc_List_Number; break;
            case 'object':
                if(f instanceof Date)
                    sortValueType_temp2 = kshf.Util.sortFunc_List_Date;
                else
                    sortValueType_temp2 = kshf.Util.sortFunc_List_Number;
                break;
            default: sortValueType_temp2 = kshf.Util.sortFunc_List_Number; break;
            }

            if(sortValueType_temp2===sortValueFunction){
                same++;
            } else {
                sortValueFunction = sortValueType_temp2;
                same=0;
            }
        }
        return sortValueFunction;
    },
    /** Updates visibility of list items */
    updateItemVisibility: function(showMoreOnly, noAnimation){
        var me = this;
        var visibleItemCount=0;

        this.DOM.listItems.each(function(item){
            var domItem = this;

            var isVisible     = (item.visibleOrder>=0) && (item.visibleOrder<me.maxVisibleItems);
            var isVisible_pre = (item.visibleOrder_pre>=0) && (item.visibleOrder_pre<me.maxVisibleItems);
            if(isVisible) {
                visibleItemCount++;
                if(me.visibleCb) me.visibleCb.call(item.data,item);
            }

            if(showMoreOnly){
                domItem.style.display = isVisible?'':'none';
                domItem.setAttribute("animSt","visible");
                return;
            }

            if(noAnimation){
                if(isVisible && !isVisible_pre){
                    domItem.style.display = '';
                    domItem.setAttribute("animSt","visible");
                }
                if(!isVisible && isVisible_pre){
                    domItem.setAttribute("animSt","closed");
                    domItem.style.display = 'none';
                }
                return;
            }

            // NOTE: Max 100 items can be under animation (visibility change), so don't worry about performance!

            if(isVisible && !isVisible_pre){
                domItem.setAttribute("animSt","closed"); // start from closed state
                setTimeout(function(){
                    domItem.style.display = '';
                    domItem.setAttribute("animSt","open");
                },500);
                setTimeout(function(){
                    domItem.setAttribute("animSt","visible");
                },1100+item.visibleOrder*20);
            }
            if(!isVisible && isVisible_pre){
                // not in view now, but in view before
                setTimeout(function(){
                    domItem.setAttribute("animSt","open");
                },-item.visibleOrder*20);
                setTimeout(function(){
                    domItem.setAttribute("animSt","closed");
                },500);
                setTimeout(function(){
                    domItem.style.display = 'none';
                },1000);
            }
            if(!isVisible && !isVisible_pre){
                domItem.style.display = 'none';
            }
        });

        var hiddenItemCount = this.browser.itemsWantedCount-visibleItemCount;
        this.DOM.showMore.select(".CountAbove").html("&#x25B2;"+visibleItemCount+" shown");
        this.DOM.showMore.select(".CountBelow").html(hiddenItemCount+" below&#x25BC;");
    },
    /** -- */
    updateAfterFilter: function(){
        if(this.recordViewSummary===null) return;
        var me=this;
        var startTime = null;
        var scrollDom = this.DOM.listItemGroup[0][0];
        var scrollInit = scrollDom.scrollTop;
        var easeFunc = d3.ease('cubic-in-out');
        var scrollTime = 1000;
        var animateToTop = function(timestamp){
            var progress;
            if(startTime===null) startTime = timestamp;
            // complete animation in 500 ms
            progress = (timestamp - startTime)/scrollTime;
            scrollDom.scrollTop = (1-easeFunc(progress))*scrollInit;
            if(scrollDom.scrollTop===0){
                me.updateVisibleIndex();
                me.updateItemVisibility(false);
            } else {
                window.requestAnimationFrame(animateToTop);
            }
        };
        window.requestAnimationFrame(animateToTop);
    },
    /** -- */
    updateVisibleIndex: function(){
        var wantedCount = 0;
        var unwantedCount = 1;
        this.browser.items.forEach(function(item){
            item.visibleOrder_pre = item.visibleOrder;
            if(item.isWanted){
                item.visibleOrder = wantedCount;
                wantedCount++;
            } else {
                item.visibleOrder = -unwantedCount;
                unwantedCount++;
            }
        });
        this.refreshRecordRanks(this.DOM.recordRanks);
        this.maxVisibleItems = this.maxVisibleItems_Default;
    }
};


kshf.Panel = function(options){
    this.browser = options.browser;
    this.name = options.name;
    this.width_catLabel = options.width_catLabel;
    this.width_catBars = 0; // placeholder
    this.width_catMeasureLabel = 1; // placeholder
    this.summaries = [];

    this.DOM = {};
    this.DOM.root = options.parentDOM.append("div")
        .attr("hasSummaries",false)
        .attr("class", "panel panel_"+options.name+
            ((options.name==="left"||options.name==="right")?" panel_side":""))
        ;
    this.initDOM_AdjustWidth();
    this.initDOM_DropZone();
};

kshf.Panel.prototype = {
    /** -- */
    getWidth_Total: function(){
        if(this.name==="bottom") return this.browser.getWidth_Total();
        return this.width_catLabel + this.width_catMeasureLabel + this.width_catBars + kshf.scrollWidth;
    },
    /** -- */
    addSummary: function(summary,index){
        var curIndex=-1;
        this.summaries.forEach(function(s,i){ if(s===summary) curIndex=i; });
        if(curIndex===-1){ // summary is new to this panel
            if(index===this.summaries.length)
                this.summaries.push(summary);
            else
                this.summaries.splice(index,0,summary);
            this.DOM.root.attr("hasSummaries",true);
            this.updateWidth_QueryPreview();
            this.refreshAdjustWidth();
        } else { // summary was in the panel. Change position
            this.summaries.splice(curIndex,1);
            this.summaries.splice(index,0,summary);
        }
        this.summaries.forEach(function(s,i){ s.panelOrder = i; });
        this.addDOM_DropZone(summary.DOM.root[0][0]);
        this.refreshAdjustWidth();
    },
    /** -- */
    removeSummary: function(summary){
        var indexFrom = -1;
        this.summaries.forEach(function(s,i){ if(s===summary) indexFrom = i; });
        if(indexFrom===-1) return; // given summary is not within this panel

        var toRemove=this.DOM.root.selectAll(".dropZone_between_wrapper")[0][indexFrom];
        toRemove.parentNode.removeChild(toRemove);

        this.summaries.splice(indexFrom,1);
        this.summaries.forEach(function(s,i){ s.panelOrder = i; });
        this.refreshDropZoneIndex();

        if(this.summaries.length===0) {
            this.DOM.root//.attr("hasSummaries",false);
                .attr("hasSummaries",false);
        } else {
            this.updateWidth_QueryPreview();
        }
        summary.panel = undefined;
        this.refreshAdjustWidth();
    },
    /** -- */
    addDOM_DropZone: function(beforeDOM){
        var me=this;
        var zone;
        if(beforeDOM){
            zone = this.DOM.root.insert("div",function(){return beforeDOM;});
        } else {
            zone = this.DOM.root.append("div");
        }
        zone.attr("class","dropZone_between_wrapper")
            .on("mouseenter",function(){
                this.setAttribute("hovered",true);
                this.children[0].setAttribute("readyToDrop",true);
            })
            .on("mouseleave",function(){
                this.setAttribute("hovered",false);
                this.children[0].setAttribute("readyToDrop",false);
            })
            .on("mouseup",function(){
                var movedSummary = me.browser.movedSummary;
                if(movedSummary.panel){ // if the summary was in the panels already
                    movedSummary.DOM.root[0][0].nextSibling.style.display = "";
                    movedSummary.DOM.root[0][0].previousSibling.style.display = "";
                }

                movedSummary.addToPanel(me,this.__data__);

                if(movedSummary.type=="categorical"){
                    movedSummary.refreshLabelWidth();
                    movedSummary.updateBarPreviewScale2Active();
                }
                movedSummary.refreshWidth();

                me.browser.updateLayout();
            })
            ;

        var zone2 = zone.append("div").attr("class","dropZone dropZone_summary dropZone_between");
        zone2.append("div").attr("class","dropIcon fa fa-angle-double-down");
        zone2.append("div").attr("class","dropText").text("Drop summary");

        this.refreshDropZoneIndex();
    },
    /** -- */
    initDOM_DropZone: function(dom){
        var me=this;
        this.DOM.dropZone_Panel = this.DOM.root.append("div").attr("class","dropZone dropZone_summary dropZone_panel")
            .attr("readyToDrop",false)
            .on("mouseenter",function(event){
                this.setAttribute("readyToDrop",true);
                this.style.width = me.getWidth_Total()+"px";
            })
            .on("mouseleave",function(event){
                this.setAttribute("readyToDrop",false);
                this.style.width = null;
            })
            .on("mouseup",function(event){
                // If this panel has summaries within, dropping makes no difference.
                if(me.summaries.length!==0) return;
                var movedSummary = me.browser.movedSummary;
                if(movedSummary===undefined) return;
                if(movedSummary.panel){ // if the summary was in the panels already
                    movedSummary.DOM.root[0][0].nextSibling.style.display = "";
                    movedSummary.DOM.root[0][0].previousSibling.style.display = "";
                }
                movedSummary.addToPanel(me);
                if(movedSummary.type=="categorical"){
                    movedSummary.refreshLabelWidth();
                    movedSummary.updateBarPreviewScale2Active();
                }
                movedSummary.refreshWidth();
                me.browser.updateLayout();
            })
            ;
        this.DOM.dropZone_Panel.append("span").attr("class","dropIcon fa fa-angle-double-down");
        this.DOM.dropZone_Panel.append("div").attr("class","dropText").text("Drop summary");

        this.addDOM_DropZone();
    },
    /** -- */
    initDOM_AdjustWidth: function(){
        if(this.name==='middle' || this.name==='bottom') return; // cannot have adjust handles for now
        var me=this;
        var root = this.browser.DOM.root;
        this.DOM.panelAdjustWidth = this.DOM.root.append("span")
            .attr("class","panelAdjustWidth")
            .on("mousedown", function (d, i) {
                if(d3.event.which !== 1) return; // only respond to left-click
                var adjustDOM = this;
                adjustDOM.setAttribute("dragging","");
                root.style('cursor','ew-resize');
                me.browser.DOM.pointerBlock.attr("active","");
                me.browser.setNoAnim(true);
                var mouseDown_x = d3.mouse(document.body)[0];
                var mouseDown_width = me.width_catBars;
                d3.select("body").on("mousemove", function() {
                    var mouseMove_x = d3.mouse(document.body)[0];
                    var mouseDif = mouseMove_x-mouseDown_x;
                    if(me.name==='right') mouseDif *= -1;
                    var oldhideBarAxis = me.hideBarAxis;
                    me.setWidthCatBars(mouseDown_width+mouseDif);
                    if(me.hideBarAxis!==oldhideBarAxis){
                        me.browser.updateLayout_Height();
                    }
                    // TODO: Adjust other panel widths
                }).on("mouseup", function(){
                    adjustDOM.removeAttribute("dragging");
                    root.style('cursor','default');
                    me.browser.DOM.pointerBlock.attr("active",null);
                    me.browser.setNoAnim(false);
                    // unregister mouse-move callbacks
                    d3.select("body").on("mousemove", null).on("mouseup", null);
                });
                d3.event.preventDefault();
            })
            .on("click",function(){
                d3.event.stopPropagation();
                d3.event.preventDefault();
            });
    },
    /** -- */
    refreshDropZoneIndex: function(){
        var me = this;
        this.DOM.root.selectAll(".dropZone_between_wrapper")
            .attr("panel_index",function(d,i){ 
                this.__data__ = i; 
                if(i===0) return "first";
                if(i===me.summaries.length) return "last";
                return "middle";
            })
            ;
    },
    /** -- */
    refreshAdjustWidth: function(){
        if(this.name==='middle' || this.name==='bottom') return; // cannot have adjust handles for now
        this.DOM.panelAdjustWidth.style("opacity",(this.summaries.length>0)?1:0);
    },
    /** -- */
    setTotalWidth: function(_w_){
        this.width_catBars = _w_-this.width_catLabel-this.width_catMeasureLabel-kshf.scrollWidth;
    },
    /** -- */
    getNumOfOpenSummaries: function(){
        return this.summaries.reduce(function(prev,cur){return prev+!cur.collapsed;},0);
    },
    /** -- */
    collapseAllSummaries: function(){
        this.summaries.forEach(function(summary){ summary.setCollapsed(true); });
    },
    /** -- */
    setWidthCatLabel: function(_w_){
        console.log(_w_);
        _w_ = Math.max(90,_w_); // use at least 90 pixels for the category label.
        if(_w_===this.width_catLabel) return;
        var widthDif = this.width_catLabel-_w_;
        this.width_catLabel = _w_;
        this.summaries.forEach(function(summary){
            if(summary.refreshLabelWidth!==undefined){
                summary.refreshLabelWidth();
            }
        });
        this.setWidthCatBars(this.width_catBars+widthDif);
    },
    /** -- */
    setWidthCatBars: function(_w_){
        _w_ = Math.max(_w_,0);
        this.hideBars = _w_<=5;
        this.hideBarAxis = _w_<=20;

        if(this.forceHideBarAxis===true){
            this.hideBarAxis = true;
        }
        if(this.hideBars===false){
            this.DOM.root.attr("hidebars",false);
        } else {
            this.DOM.root.attr("hidebars",true);
        }
        if(this.hideBarAxis===false){
            this.DOM.root.attr("hideBarAxis",false);
        } else {
            this.DOM.root.attr("hideBarAxis",true);
        }

        this.width_catBars = _w_;

        this.updateSummariesWidth();
        if(this.name!=="middle")
            this.browser.updateMiddlePanelWidth();
    },
    /** --- */
    updateSummariesWidth: function(){
        this.summaries.forEach(function(summary){
            if(summary.hasCategories && summary.hasCategories()){
                summary.updateBarPreviewScale2Active();
            }
            summary.refreshWidth();
        });
    },
    /** --- */
    updateWidth_QueryPreview: function(){
        var maxTotalCount = d3.max(this.summaries, function(summary){
            if(summary.getMaxAggr_Total===undefined) return 0;
            return summary.getMaxAggr_Total();
        });

        var oldPreviewWidth = this.width_catMeasureLabel;

        this.width_catMeasureLabel = 13;
        var digits = 1;
        while(maxTotalCount>9){
            digits++;
            maxTotalCount = Math.floor(maxTotalCount/10);
        }
        if(digits>3) {
            digits = 2;
            this.width_catMeasureLabel+=4; // "." character is used to split. It takes some space
        }
        this.width_catMeasureLabel += digits*6;

        if(oldPreviewWidth!==this.width_catMeasureLabel){
            this.summaries.forEach(function(summary){
                if(summary.refreshLabelWidth) summary.refreshLabelWidth();
            });
        }
    }
};

/**
 * @constructor
 */
kshf.Browser = function(options){  
    this.options = options;
    
    if(kshf.lang.cur===null){
        kshf.lang.cur = kshf.lang.en;
    }

    // BASIC OPTIONS
    this.summaries = [];
    this.summaries_by_name = {};
    this.panels = {};

    this.selfRefSummaries = [];
    this.maxFilterID = 0;

    this.filters = [];

    this.attribsShown = false;

    this.pauseResultPreview = false;
    this.vizPreviewActive = false;
    this.vizCompareActive = false;
    this.ratioModeActive = false;
    this.percentModeActive = false;
    this.isFullscreen = false;

    this.previewedSelectionSummary = null;

    this.noAnim=false;

    this.listDef = options.itemDisplay || {};
    if(options.list) this.listDef = options.list;

    this.domID = options.domID;

    // Callbacks
    this.loadedCb = options.loadedCb;
    this.newSummaryCb = options.newSummaryCb;
    this.readyCb = options.readyCb;
    this.updateCb = options.updateCb;
    this.previewCb = options.previewCb;
    this.previewCompareCb = options.previewCompareCb;
    this.preview_not = false;
    this.ratioModeCb = options.ratioModeCb;

    this.showDropZones = false;

    this.itemName = options.itemName || "";

    this.showDataSource = true;
    if(options.showDataSource===false) this.showDataSource = false;

    this.forceHideBarAxis = false;
    if(options.forceHideBarAxis!==undefined) this.forceHideBarAxis = options.forceHideBarAxis;
    this.DOM = {};
    this.DOM.root = d3.select(this.domID)
        .classed("kshf",true)
        .attr("percentview",false)
        .attr("noanim",true)
        .attr("ratiomode",false)
        .attr("attribsShown",false)
        .attr("showdropzone",false)
        .attr("previewcompare",false)
        .attr("resultpreview",false)
        .style("position","relative")
        //.style("overflow-y","hidden")
        .on("mousemove",function(d){
            if(typeof logIf === "object"){
                logIf.setSessionID();
            }
        })
        ;

    // remove any DOM elements under this domID, kshf takes complete control over what's inside
    var rootDomNode = this.DOM.root[0][0];
    while (rootDomNode.hasChildNodes()) rootDomNode.removeChild(rootDomNode.lastChild);

    this.DOM.pointerBlock  = this.DOM.root.append("div").attr("class","pointerBlock");
    this.DOM.attribDragBox = this.DOM.root.append("div").attr("class","attribDragBox");

    this.insertDOM_ResizeBrowser();
    this.insertDOM_Infobox();
    this.insertDOM_WarningBox();

    this.insertDOM_PanelBasic();

    this.DOM.panelsTop = this.DOM.root.append("div").attr("class","panels_Above");

    this.panels.left = new kshf.Panel({
        width_catLabel : options.leftPanelLabelWidth  || options.categoryTextWidth || 115,
        browser: this,
        name: 'left',
        parentDOM: this.DOM.panelsTop
    });

    this.DOM.middleColumn = this.DOM.panelsTop.append("div").attr("class","middleColumn");

    this.DOM.middleColumn.append("div").attr("class", "recordDisplay")

    this.panels.middle = new kshf.Panel({
        width_catLabel : options.middlePanelLabelWidth  || options.categoryTextWidth || 115,
        browser: this,
        name: 'middle',
        parentDOM: this.DOM.middleColumn
    });
    this.panels.right = new kshf.Panel({
        width_catLabel : options.rightPanelLabelWidth  || options.categoryTextWidth || 115,
        browser: this,
        name: 'right',
        parentDOM: this.DOM.panelsTop
    });
    this.panels.bottom = new kshf.Panel({
        width_catLabel : options.categoryTextWidth || 115,
        browser: this,
        name: 'bottom',
        parentDOM: this.DOM.root
    });

    this.DOM.attributePanel = this.DOM.root.append("div").attr("class","panel attributePanel");
    var xx= this.DOM.attributePanel.append("div").attr("class","attributePanelHeader");
    xx.append("span").text("Available Attributes");
    xx.append("span").attr("class","addAttrib fa fa-plus")
        .each(function(){
            this.tipsy = new Tipsy(this, {
                gravity: "e",
                title: function(){ return "Add new"; }
            })
        })
        .on("mouseover",function(){ this.tipsy.show(); })
        .on("mouseout" ,function(){ this.tipsy.hide(); })
        .on("click",function(){
            me.createSummary("[New]",function(){ return this.Name;}, 'categorical');
            me.insertAttributeList();
        });
    xx.append("span").attr("class","hidePanel fa fa-times")
        .each(function(){
            this.tipsy = new Tipsy(this, {
                gravity: "e",
                title: function(){ return "Close panel"; }
            })
        })
        .on("mouseover",function(){ this.tipsy.show(); })
        .on("mouseout" ,function(){ this.tipsy.hide(); })
        .on("click",function(){
            me.showAttributes();
        });

    this.DOM.attributeList = this.DOM.attributePanel.append("div").attr("class","attributeList");

    this.DOM.dropZone_AttribList = this.DOM.attributeList.append("div").attr("class","dropZone dropZone_AttribList")
        .attr("readyToDrop",false)
        .on("mouseenter",function(event){
            this.setAttribute("readyToDrop",true);
        })
        .on("mouseleave",function(event){
            this.setAttribute("readyToDrop",false);
        })
        .on("mouseup",function(event){
            var movedSummary = me.movedSummary;
            movedSummary.removeFromPanel();
            movedSummary.clearDOM();
            movedSummary.browser.updateLayout();
            me.movedSummary = null;
        })
        ;
    this.DOM.dropZone_AttribList.append("span").attr("class","dropIcon fa fa-angle-double-down");
    this.DOM.dropZone_AttribList.append("div").attr("class","dropText").text("Remove summary");

    var me = this;

    this.DOM.root.selectAll(".panel").on("mouseleave",function(){
        setTimeout( function(){ me.updateLayout_Height(); }, 1500); // update layout after 1.5 seconds
    });

    if(options.source){       
        window.setTimeout(function() { me.loadSource(options.source); }, 10);                
    } else {
        this.panel_infobox.attr("show","source");
    }

    kshf.loadFont();
};

kshf.Browser.prototype = {
    /** -- */
    setNoAnim: function(v){
        if(v===this.noAnim) return;
        if(this.finalized===undefined) return;
        this.noAnim=v;
        this.DOM.root.attr("noanim",this.noAnim);
    },
    /** -- */
    removeSummary: function(summary){
        var indexFrom = -1;
        this.summaries.forEach(function(s,i){
            if(s===summary) indexFrom = i;
        });
        if(indexFrom===-1) return; // given summary is not within this panel
        this.summaries.splice(indexFrom,1);

        summary.removeFromPanel();
    },
    /** -- */
    getAttribTypeFromFunc: function(attribFunc){
        var type = null;
        this.items.some(function(item,i){
            var item=attribFunc.call(item.data,item);
            if(item===null) return false;
            if(item===undefined) return false;
            if(typeof(item)==="number" || item instanceof Date) {
                type="interval";
                return true;
            }
            // TODO": Think about boolean summaries
            if(typeof(item)==="string" || typeof(item)==="boolean") {
                type = "categorical";
                return true;
            }
            if(Array.isArray(item)){
                type = "categorical";
                return true;
            }
            return false;
        },this);
        return type;
    },
    /** -- */
    createSummary: function(name,func,type){
        if(this.summaries_by_name[name]!==undefined){
            console.log("createSummary: The summary name["+name+"] is already used. It must be unique. Try again");
            return;
        }
        if(typeof(func)==="string"){
            var x=func;
            func = function(){ return this[x]; }
        }

        var attribFunc=func || function(d){ return d.data[name]; }
        if(type===undefined){
            type = this.getAttribTypeFromFunc(attribFunc);
        }
        if(type===null){
            console.log("Summary data type could not be detected for summary name:"+name);
            return;
        }

        var summary;
        if(type==='categorical'){
            summary = new kshf.Summary_Categorical();
        }
        if(type==='interval'){
            summary = new kshf.Summary_Interval();
        }

        summary.initialize(this,name,func);

        this.summaries.push(summary);
        this.summaries_by_name[name] = summary;

        if(this.newSummaryCb) this.newSummaryCb.call(this,summary);
        return summary;
    },
    /** -- */
    changeSummaryName: function(curName,newName){
        if(curName===newName) return;
        var summary = this.summaries_by_name[curName];
        if(summary===undefined){
            console.log("The given summary name is not there. Try again");
            return;
        }
        if(this.summaries_by_name[newName]!==undefined){
            if(newName!==this.summaries_by_name[newName].summaryColumn){
                console.log("The new summary name is already used. It must be unique. Try again");
                return;
            }
        }
        // remove the indexing using oldName IFF the old name was not original column name
        if(curName!==summary.summaryColumn){
            delete this.summaries_by_name[curName];
        }
        this.summaries_by_name[newName] = summary;
        summary.setSummaryName(newName);
        return summary;
    },
    /** -- */
    getWidth_Total: function(){
        return this.divWidth;
    },
    /** -- */
    domHeight: function(){
        return parseInt(this.DOM.root.style("height"));
    },
    /** -- */
    domWidth: function(){
        return parseInt(this.DOM.root.style("width"));
    },
    // TODO: If names are the same and config options are different, what do you do?
    createFilter: function(opts){
        opts.browser = this;
        // see if it has been created before TODO
        var newFilter = new kshf.Filter(this.maxFilterID,opts);
        ++this.maxFilterID;
        this.filters.push(newFilter);
        return newFilter;
    },
    /** -- */
    insertDOM_ResizeBrowser: function(){
        var me=this;
        this.DOM.resizeBrowser_corner = this.DOM.root.append("div").attr("class", "resizeBrowser_corner")
            .each(function(summary){
                this.tipsy = new Tipsy(this, {
                    gravity: 'e', title: function(){ return kshf.lang.cur.ResizeBrowser; }
                });
            })
            .on("mouseover",function(){
                if(this.getAttribute("dragging")==="true") return;
                this.tipsy.show();
            })
            .on("mouseout",function(){
                this.tipsy.hide();
            })
            .on("mousedown", function (d, i) {
                var resizeDOM = this;
                this.tipsy.hide();
                resizeDOM.setAttribute("dragging",true);
                me.DOM.root.style('cursor','nwse-resize');
                me.setNoAnim(true);
                var mouseDown_x = d3.mouse(d3.select("body")[0][0])[0];
                var mouseDown_y = d3.mouse(d3.select("body")[0][0])[1];
                var mouseDown_width  = parseInt(d3.select(this.parentNode).style("width"));
                var mouseDown_height = parseInt(d3.select(this.parentNode).style("height"));
                d3.select("body").on("mousemove", function() {
                    var mouseDown_x_diff = d3.mouse(d3.select("body")[0][0])[0]-mouseDown_x;
                    var mouseDown_y_diff = d3.mouse(d3.select("body")[0][0])[1]-mouseDown_y;
                    d3.select(me.domID).style("height",(mouseDown_height+mouseDown_y_diff)+"px");
                    d3.select(me.domID).style("width" ,(mouseDown_width +mouseDown_x_diff)+"px");
                    me.updateLayout();
                }).on("mouseup", function(){
                    if(sendLog) sendLog(kshf.LOG.RESIZE);
                    resizeDOM.removeAttribute("dragging");
                    me.DOM.root.style('cursor','default');
                    me.setNoAnim(false);
                    // unregister mouse-move callbacks
                    d3.select("body").on("mousemove", null).on("mouseup", null);
                });
               d3.event.preventDefault();
            })
            .style("display",this.options.showResizeCorner?true:false);
    },
    /* -- */
    insertDOM_WarningBox: function(){
        this.panel_warningBox = this.DOM.root.append("div").attr("class", "warningBox_wrapper").attr("shown",false)
        var x = this.panel_warningBox.append("span").attr("class","warningBox");
        this.DOM.warningText = x.append("span").attr("class","warningText");
        x.append("span").attr("class","dismiss").text("Dismiss")
            .on("click",function(){
                this.parentNode.parentNode.setAttribute("shown",false);
            });
    },
    /** -- */
    showWarning: function(v){
        this.panel_warningBox.attr("shown",true);
        this.DOM.warningText.text(v);
    },
    /** -- */
    hideWarning: function(){
        this.panel_warningBox.attr("shown",false);
    },
    /** -- */
    insertDOM_PanelBasic: function(){
        var me=this;

        this.DOM.panel_Basic = this.DOM.root.append("div").attr("class","panel_Basic");

        var recordInfo = this.DOM.panel_Basic.append("span")
            .attr("class","recordInfo editableTextContainer")
            .attr("edittitle",false);

        this.DOM.activeRecordCount = recordInfo.append("span").attr("class","activeRecordCount");

        this.DOM.recordName = recordInfo.append("span").attr("class","recordName editableText")
            .attr("contenteditable",false)
            .on("mousedown", function(){ d3.event.stopPropagation(); })
            .on("blur",function(){
                this.parentNode.setAttribute("edittitle",false);
                this.setAttribute("contenteditable", false);
                me.itemName = this.textContent;
            })
            .on("keydown",function(){
                if(event.keyCode===13){ // ENTER
                    this.parentNode.setAttribute("edittitle",false);
                    this.setAttribute("contenteditable", false);
                    me.itemName = this.textContent;
                }
            });

        recordInfo.append("span")
            .attr("class","editTextButton fa")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){
                        var curState=this.parentNode.getAttribute("edittitle");
                        if(curState===null || curState==="false"){
                            return kshf.lang.cur.EditTitle;
                        } else {
                            return "OK";
                        }
                    }
                })
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                d3.event.stopPropagation();
                d3.event.preventDefault();
            })
            .on("click",function(){
                var curState=this.parentNode.getAttribute("edittitle");
                if(curState===null || curState==="false"){
                    this.parentNode.setAttribute("edittitle",true);
                    var parentDOM = d3.select(this.parentNode);
                    var v=parentDOM.select(".recordName")[0][0];
                    v.setAttribute("contenteditable",true);
                    v.focus();
                } else {
                    this.parentNode.setAttribute("edittitle",false);
                    var parentDOM = d3.select(this.parentNode);
                    var v=parentDOM.select(".recordName")[0][0];
                    v.setAttribute("contenteditable",false);
                    me.itemName = this.textContent;
                }
            });

        this.DOM.filtercrumbs = this.DOM.panel_Basic.append("span").attr("class","filtercrumbs");

        this.initDOM_ClearAllFilters();

        var rightBoxes = this.DOM.panel_Basic.append("span").attr("class","rightBoxes");
        // Attribute panel
        rightBoxes.append("i").attr("class","showConfigButton fa fa-cog")
            .each(function(d){
                this.tipsy = new Tipsy(this, { gravity: 'ne', title: function(){ return kshf.lang.cur.ModifyBrowser; } });
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout", function(){ this.tipsy.hide(); })
            .on("click",function(){ me.showAttributes(); })
            ;
        // Datasource
        this.DOM.datasource = rightBoxes.append("a").attr("class","fa fa-table datasource")
            .attr("target","_blank")
            .each(function(d){
                this.tipsy = new Tipsy(this, { gravity: 'ne', title: function(){ return kshf.lang.cur.OpenDataSource; } });
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout",function(d,i){ this.tipsy.hide(); })
            .on("click",function(){
                if(sendLog) sendLog(kshf.LOG.DATASOURCE);
            })
            ;
        // Info & Credits
        rightBoxes.append("i").attr("class","fa fa-info-circle credits")
            .each(function(d){
                this.tipsy = new Tipsy(this, { gravity: 'ne', title: function(){ return kshf.lang.cur.ShowInfoCredits; } });
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout",function(d,i){ this.tipsy.hide(); })
            .on("click",function(){ me.showInfoBox();})
            ;
        // Info & Credits
        rightBoxes.append("i").attr("class","fa fa-arrows-alt fullscreen")
            .each(function(d){
                this.tipsy = new Tipsy(this, { gravity: 'ne', title: function(){ return kshf.lang.cur.ShowFullscreen; } });
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout",function(d,i){ this.tipsy.hide(); })
            .on("click",function(){ me.showFullscreen();})
            ;

        var adsdasda = this.DOM.panel_Basic.append("div").attr("class","totalViz");
        this.DOM.totalViz_total = adsdasda.append("span").attr("class","aggr total");
        this.DOM.totalViz_active = adsdasda.append("span").attr("class","aggr active");
        this.DOM.totalViz_preview = adsdasda.append("span").attr("class","aggr preview");
    },
    /** -- */
    refreshTotalViz: function(){
        this.DOM.totalViz_active .style("width",
            (100*this.itemsWanted_Aggregrate_Total/this.itemsTotal_Aggregrate_Total)+"%");
        this.DOM.totalViz_preview.style("width",
            (100*this.itemCount_Previewed/this.itemsTotal_Aggregrate_Total)+"%");
    },
    /** --- */
    initDOM_ClearAllFilters: function(){
        var me=this;
        this.DOM.filterClearAll = this.DOM.panel_Basic.append("span").attr("class","filterClearAll")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: 'n', title: function(){ return kshf.lang.cur.RemoveAllFilters; }
                });
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("click",function(){
                this.tipsy.hide();
                me.clearFilters_All();
            })
            ;
        this.DOM.filterClearAll.append("span").attr("class","title").text(kshf.lang.cur.ShowAll);
        this.DOM.filterClearAll.append("div").attr("class","chartClearFilterButton allFilter")
            .append("span").attr("class","fa fa-times")
            ;
    },
    /* -Modified to show the i3visio credits- */
    insertDOM_Infobox: function(){
        var me=this;
        /* TO-DO: update the language depending on the language */
        var creditString="";
        creditString += "<div align='center'>";
        creditString += "<div class='header'>Explorify is part of <span class='libName'>OSRFramework</span>.</div>";
        creditString += "<div align='center' class='boxinbox project_credits'>";
        creditString += "<div>Developed by</div>";
        //creditString += " <a href='http://www.cs.umd.edu/hcil/' target='_blank'><img src='https://wiki.umiacs.umd.edu/hcil/images/1/10/HCIL_logo_small_no_border.gif' style='height:50px'></a>";
        creditString += " Yaiza Rubio and Félix Brezo</br><a class='myName' href='http://i3visio.com' target='_blank'>i3visio</a>";
        //creditString += " <a href='http://www.umd.edu' target='_blank'><img src='http://www.trademarks.umd.edu/marks/gr/informal.gif' style='height:50px'></a>";
        creditString += "</div>";
        creditString += "";
        creditString += "<div align='center' class='boxinbox project_credits'>";
            creditString += "<div style='float:right; text-align: right'>"
            creditString += "<iframe src='http://ghbtns.com/github-btn.html?user=i3visio&repo=osrframework&type=watch&count=true' allowtransparency='true' frameborder='0' scrolling='0' width='90px' height='20px'></iframe><br/>";
            creditString += "</div>";
            creditString += "<div style='float:left; padding-left: 10px'>"
            creditString += "<iframe src='http://ghbtns.com/github-btn.html?user=i3visio&repo=osrframework&type=fork&count=true' allowtransparency='true' frameborder='0' scrolling='0' width='90px' height='20px'></iframe>";
            creditString += "</div>";
        creditString += "Libraries and third-party used:<br/>";
        creditString += " <a href='http://d3js.org/' target='_blank'>D3</a> -";
        creditString += " <a href='http://jquery.com' target='_blank'>JQuery</a> -";
        creditString += " <a href='https://github.com/adilyalcin/keshif' target='_blank'>Keshif</a>";
        creditString += "</div><br/>";
        //creditString += "";
        creditString += "<div align='center' class='project_fund'>";
        creditString += "If you have questions or if you just want to know what things we do, <br/>";
        creditString += "you can contact us in <a href='mailto:contacto@i3visio.com'>contacto@i3visio.com</a>.</div>";
        //creditString += "";

        this.panel_infobox = this.DOM.root.append("div").attr("class", "panel panel_infobox");
        this.panel_infobox.append("div").attr("class","background")
            .on("click",function(){
                var activePanel = this.parentNode.getAttribute("show");
                if(activePanel==="credit" || activePanel==="itemZoom"){
                    me.panel_infobox.attr("show","none");
                }
            })
            ;
        this.DOM.loadingBox = this.panel_infobox.append("div").attr("class","infobox_content infobox_loading");
//        this.DOM.loadingBox.append("span").attr("class","fa fa-spinner fa-spin");
        var ssdsd = this.DOM.loadingBox.append("span").attr("class","spinner");
        ssdsd.append("span").attr("class","spinner_x spinner_1");
        ssdsd.append("span").attr("class","spinner_x spinner_2");
        ssdsd.append("span").attr("class","spinner_x spinner_3");
        ssdsd.append("span").attr("class","spinner_x spinner_4");
        ssdsd.append("span").attr("class","spinner_x spinner_5");

        var hmmm=this.DOM.loadingBox.append("div").attr("class","status_text");
        hmmm.append("span").attr("class","status_text_sub info").text(kshf.lang.cur.LoadingData);
        this.DOM.status_text_sub_dynamic = hmmm.append("span").attr("class","status_text_sub dynamic");

        var infobox_credit = this.panel_infobox.append("div").attr("class","infobox_content infobox_credit");
        infobox_credit.append("div").attr("class","infobox_close_button")
            .on("click",function(){
                me.panel_infobox.attr("show","none");
            })
            .append("span").attr("class","fa fa-times");
        infobox_credit.append("div").attr("class","all-the-credits").html(creditString);

        this.insertSourceBox();


        this.DOM.infobox_itemZoom = this.panel_infobox.append("span").attr("class","infobox_content infobox_itemZoom");

        this.DOM.infobox_itemZoom.append("div").attr("class","infobox_close_button")
            .on("click",function(){
                me.panel_infobox.attr("show","none");
            })
            .append("span").attr("class","fa fa-times");

        this.DOM.infobox_itemZoom_content = this.DOM.infobox_itemZoom.append("span").attr("class","content");
    },
    /** -- */
    insertSourceBox: function(){
        var me=this;
        var x,y,z;
        var source_type="GoogleSheet";
        var sourceURL=null, sourceSheet="";

        var readyToLoad=function(){
            return sourceURL!==null && sourceSheet!=="";
        };

        this.DOM.infobox_source = this.panel_infobox.append("div").attr("class","infobox_content infobox_source")
            .attr("selected_source_type",source_type);

        this.DOM.infobox_source.append("div").attr("class","sourceHeader").text("Where's your data?");

        var source_wrapper = this.DOM.infobox_source.append("div").attr("class","source_wrapper");

        x = source_wrapper.append("div").attr("class","offpoofff");

        x.append("span").attr("class","source_from").text("Google Sheet").attr("source_type","GoogleSheet");
        x.append("span").attr("class","source_from").text("Google Drive Folder").attr("source_type","GoogleDrive");
        x.append("span").attr("class","source_from").text("Dropbox Folder").attr("source_type","Dropbox");
        x.append("span").attr("class","source_from").text("Local File").attr("source_type","LocalFile");

        x.selectAll(".source_from").on("click",function(){
            source_type=this.getAttribute("source_type");
            me.DOM.infobox_source.attr("selected_source_type",source_type);
            var placeholder;
            switch(source_type){
                case "GoogleSheet": placeholder = 'https://docs.google.com/spreadsheets/d/**************'; break;
                case "GoogleDrive": placeholder = 'https://******.googledrive.com/host/**************/'; break;
                case "Dropbox": placeholder = "https://dl.dropboxusercontent.com/u/**************/";
            }
            
            gdocLink.attr("placeholder",placeholder);
        });

        x = source_wrapper.append("div");
        var gdocLink = x.append("input")
            .attr("type","text")
            .attr("class","gdocLink")
            .attr("placeholder",'https://docs.google.com/spreadsheets/d/**************')
            .on("keyup",function(){
                gdocLink_ready.style("opacity",this.value===""?"0":"1");
                var input = this.value;
                if(source_type==="GoogleSheet"){
                    var firstIndex = input.indexOf("docs.google.com/spreadsheets/d/");
                    if(firstIndex!==-1){
                        var input = input.substr(firstIndex+31); // focus after the base url
                        if(input.indexOf("/")!==-1){
                            input = input.substr(0,input.indexOf("/"));
                        }
                    }
                    if(input.length===44){
                        sourceURL = input;
                        gdocLink_ready.attr("ready",true);
                    } else {
                        sourceURL = null;
                        gdocLink_ready.attr("ready",false);
                    }
                }
                if(source_type==="GoogleDrive"){
                    var firstIndex = input.indexOf(".googledrive.com/host/");
                    if(firstIndex!==-1){
                        // Make sure last character is "/"
                        if(input[input.length-1]!=="/") input+="/";
                        sourceURL = input;
                        gdocLink_ready.attr("ready",true);
                    } else{
                        sourceURL = null;
                        gdocLink_ready.attr("ready",false);
                    }
                }
                if(source_type==="Dropbox"){
                    var firstIndex = input.indexOf("dl.dropboxusercontent.com/");
                    if(firstIndex!==-1){
                        // Make sure last character is "/"
                        if(input[input.length-1]!=="/") input+="/";
                        sourceURL = input;
                        gdocLink_ready.attr("ready",true);
                    } else{
                        sourceURL = null;
                        gdocLink_ready.attr("ready",false);
                    }
                }
                if(source_type==="LocalFile"){
                    // TODO              
                }
                actionButton.attr("disabled",!readyToLoad());
            });

        x.append("span").attr("class","fa fa-info-circle")
                .each(function(summary){
                    this.tipsy = new Tipsy(this, {
                        gravity: 's', title: function(){
                            if(source_type==="GoogleSheet")
                                return "The link to your Google Sheet";
                            if(source_type==="GoogleDrive")
                                return "The link to *hosted* Google Drive folder";
                            if(source_type==="Dropbox")
                                return "The link to your *Public* Dropbox folder";
                            if(source_type==="LocalFile")
                                return "Select your file or drag & drop into the field";
                        }
                    });
                })
                .on("mouseenter",function(){ this.tipsy.show(); })
                .on("mouseleave",function(){ this.tipsy.hide(); });

        var gdocLink_ready = x.append("span").attr("class","gdocLink_ready fa").attr("ready",false);

        var sheetInfo = this.DOM.infobox_source.append("div").attr("class","sheetInfo");

        x = sheetInfo.append("div").attr("class","sheet_wrapper")
            x.append("div").attr("class","subheading tableHeader")
            ;

        x = sheetInfo.append("div").attr("class","sheet_wrapper sheetName_wrapper")
            x.append("span").attr("class","subheading").text("Name");
            x.append("span").attr("class","fa fa-info-circle")
                .each(function(summary){
                    this.tipsy = new Tipsy(this, {
                        //gravity: 's', title: function(){ return "Your document may have multiple sheets.<br>Provide the name of the main sheet"; }
                        gravity: 's', title: function(){
                            var v;
                            if(source_type==="GoogleSheet")
                                v="The name of the data sheet in your Google Sheet.";
                            if(source_type==="GoogleDrive")
                                v="The file name in the folder.";
                            if(source_type==="Dropbox")
                                v="The file name in the folder.";
                            v+="<br>Also describes what each data row represents"
                            return v;
                        }
                    });
                })
                .on("mouseenter",function(){ this.tipsy.show(); })
                .on("mouseleave",function(){ this.tipsy.hide(); });

            x.append("input").attr("type","text").attr("class","sheetName")
                .on("keyup",function(){
                    sourceSheet = this.value;
                    actionButton.attr("disabled",!readyToLoad());
                });
            z=x.append("span").attr("class","fileType_wrapper");
            z.append("span").text(".");
            var DOMfileType = z.append("select").attr("class","fileType");
                DOMfileType.append("option").attr("value","csv").text("csv");
                DOMfileType.append("option").attr("value","tsv").text("tsv");
                DOMfileType.append("option").attr("value","json").text("json");

        x = sheetInfo.append("div").attr("class","sheet_wrapper sheetColumn_ID_wrapper")
            x.append("span").attr("class","subheading").text("ID column");
            x.append("span").attr("class","fa fa-info-circle")
                .each(function(summary){
                    this.tipsy = new Tipsy(this, {
                        //gravity: 's', title: function(){ return "Your document may have multiple sheets.<br>Provide the name of the main sheet"; }
                        gravity: 's', title: function(){ return "The column that uniquely identifies each item.<br><br>If no such column, skip."; }
                    });
                })
                .on("mouseenter",function(){ this.tipsy.show(); })
                .on("mouseleave",function(){ this.tipsy.hide(); });
            x.append("input").attr("class","sheetColumn_ID").attr("type","text").attr("placeholder","id");

        x = sheetInfo.append("div").attr("class","sheet_wrapper sheetColumn_Split_wrapper")
            x.append("span").attr("class","subheading").text("Split column");
            x.append("span").attr("class","fa fa-info-circle")
                .each(function(summary){
                    this.tipsy = new Tipsy(this, {
                        //gravity: 's', title: function(){ return "Your document may have multiple sheets.<br>Provide the name of the main sheet"; }
                        gravity: 's', title: function(){
                            return "If column has multi-values<br>(ex: action+drama),<br>split values using separator";
                        }
                    });
                })
                .on("mouseenter",function(){ this.tipsy.show(); })
                .on("mouseleave",function(){ this.tipsy.hide(); });
            x.append("input").attr("type","text").attr("class","sheetColumn_Splitter")
                .on("keyup",function(){
                    sheetColumn_sep_wrapper.style("display",this.value!==""?"inline-block":"none");
                });
            var sheetColumn_sep_wrapper = x.append("span").attr("class","sheetColumn_sep_wrapper");
                sheetColumn_sep_wrapper.append("span").text(" with")
                sheetColumn_sep_wrapper.append("span").attr("class","fa fa-info-circle")
                    .each(function(summary){
                        this.tipsy = new Tipsy(this, {
                            //gravity: 's', title: function(){ return "Your document may have multiple sheets.<br>Provide the name of the main sheet"; }
                            gravity: 's', title: function(){
                                return "Separator";
                            }
                        });
                    })
                    .on("mouseenter",function(){ this.tipsy.show(); })
                    .on("mouseleave",function(){ this.tipsy.hide(); });;
                sheetColumn_sep_wrapper.append("input").attr("class","sheetColumn_Separator").attr("type","text").attr("placeholder","+");


        var actionButton = this.DOM.infobox_source.append("div").attr("class","actionButton")
            .html("Explore it with Keshif")
            .attr("disabled",true)
            .on("click",function(){
                if(!readyToLoad()){
                    alert("Please input your data source link and sheet name.");
                    return;
                }
                var sheetID   = me.DOM.infobox_source.select(".sheetColumn_ID")[0][0].value;
                if(sheetID==="") sheetID = "id";
                var loadedCb_pre = me.loadedCb;
                me.loadedCb = function(){
                    var splitColumnName = me.DOM.infobox_source.select(".sheetColumn_Splitter")[0][0].value;
                    var splitSepName = me.DOM.infobox_source.select(".sheetColumn_Separator")[0][0].value;
                    if(splitColumnName){
                        kshf.Util.cellToArray(this.items, [splitColumnName], splitSepName, false);
                    }
                    if(loadedCb_pre) loadedCb_pre.call(this,this);
                };
                var readyCb_pre = me.readyCb;
                me.readyCb = function(){
                    me.showAttributes();
                    if(readyCb_pre) readyCb_pre.call(this,this);
                }
                if(source_type==="GoogleSheet"){
                    me.loadSource({
                        gdocId: sourceURL,
                        sheets: [ {name:sourceSheet, id:sheetID} ]
                    });
                }
                if(source_type==="GoogleDrive"){
                    me.loadSource({
                        dirPath: sourceURL,
                        fileType: DOMfileType[0][0].value,
                        sheets: [ {name:sourceSheet, id:sheetID} ]
                    });
                }
                if(source_type==="Dropbox"){
                    me.loadSource({
                        dirPath: sourceURL,
                        fileType: DOMfileType[0][0].value,
                        sheets: [ {name:sourceSheet, id:sheetID} ]
                    });
                }
                if(source_type==="LocalFile"){
                    me.loadSource({
                        dirPath: sourceURL,
                        fileType: DOMfileType[0][0].value,
                        sheets: [ {name:sourceSheet, id:sheetID} ]
                    });
                }
            });
    },
    /** -- */
    updateItemZoomText: function(item){
        var str="";
        for(var column in item.data){
            var v=item.data[column];
            if(v===undefined || v===null) continue;
            str+="<b>"+column+":</b> "+ v.toString()+"<br>";
        }
        this.DOM.infobox_itemZoom_content.html(str);
//        this.DOM.infobox_itemZoom_content.html(item.data.toString());
    },
    /** -- */
    showAttributes: function(v){
        if(v===undefined) v = !this.attribsShown; // if undefined, invert
        this.attribsShown = v;
        this.DOM.root.attr("attribsShown",this.attribsShown);

        var lastIndex = 0, me=this;
        var initAttib = function(){
            var start = Date.now();
            me.summaries[lastIndex++].initializeAggregates();
            var end = Date.now();
            if(lastIndex!==me.summaries.length)
                setTimeout(initAttib,end-start);
        };
        setTimeout(initAttib,150);
    },
    /** -- */
    showFullscreen: function(){
        this.isFullscreen = this.isFullscreen?false:true;
        var elem = browser.DOM.root[0][0];
        if(this.isFullscreen){
            if (elem.requestFullscreen) {
              elem.requestFullscreen();
            } else if (elem.msRequestFullscreen) {
              elem.msRequestFullscreen();
            } else if (elem.mozRequestFullScreen) {
              elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullscreen) {
              elem.webkitRequestFullscreen();
            }
        } else {
            if (document.exitFullscreen) {
              document.exitFullscreen();
            } else if (document.msExitFullscreen) {
              document.msExitFullscreen();
            } else if (document.mozCancelFullScreen) {
              document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) {
              document.webkitExitFullscreen();
            }
        }
    },
    /** -- */
    showInfoBox: function(){
        this.panel_infobox.attr("show","credit");
        if(sendLog) sendLog(kshf.LOG.INFOBOX);
    },
    /** -- */
    loadSource: function(v){
        this.source = v;
        this.panel_infobox.attr("show","loading");
        if(this.source.sheets){
            if(!Array.isArray(this.source.sheets)){
                this.source.sheets = [this.source.sheets];
            }
            this.source.sheets.forEach(function(sheet, i){
                if(typeof sheet === "string"){
                    this.source.sheets[i] = {name: sheet};
                }
            }, this);
            this.source.loadedTableCount=0;

            this.DOM.status_text_sub_dynamic
                .text("("+this.source.loadedTableCount+"/"+this.source.sheets.length+")");

            this.source.sheets[0].primary = true;
            this.primaryTableName = this.source.sheets[0].name;
            if(this.source.gdocId){
                if(this.source.url===undefined)
                    this.source.url = "https://docs.google.com/spreadsheet/ccc?key="+this.source.gdocId;
            }
            this.source.sheets.forEach(function(sheet){
                if(sheet.id===undefined) sheet.id="id"; // set id column
                if(sheet.tableName===undefined) sheet.tableName = sheet.name; // set table name
                // if this table name has been loaded, skip this one
                if(kshf.dt[sheet.tableName]!==undefined){
                    this.incrementLoadedSheetCount();
                    return;
                }
                if(this.source.gdocId){
                    this.loadSheet_Google(sheet);
                } else if(this.source.dirPath){
                    if(this.source.fileType==="json"){
                        this.loadSheet_JSON(sheet);
                    } else if(this.source.fileType==="csv" || this.source.fileType==="tsv"){
                        this.loadSheet_CSV(sheet);
                    }
                }
            },this);
        } else {
            if(this.source.callback){
                this.source.callback(this);
            }
        }
    },
    loadSheet_Google: function(sheet){
        var me=this;
        var headers=1;
        if(sheet.headers){
            headers = sheet.headers;
        }
        var qString='https://docs.google.com/spreadsheet/tq?key='+this.source.gdocId+'&headers='+headers;
        if(sheet.sheetID){
            qString+='&gid='+sheet.sheetID;
        } else {
            qString+='&sheet='+sheet.name;
        }
        if(sheet.range){
            qString+="&range="+sheet.range;
        }

        var googleQuery = new google.visualization.Query(qString);
        if(sheet.query) googleQuery.setQuery(sheet.query);

        googleQuery.send( function(response){
            if(kshf.dt[sheet.tableName]!==undefined){
                me.incrementLoadedSheetCount();
                return;
            }
            if(response.isError()) {
                me.panel_infobox.select("div.status_text .info")
                    .text("Cannot load data");
                me.panel_infobox.select("span.spinner").selectAll("span").remove();
                me.panel_infobox.select("span.spinner").append('i').attr("class","fa fa-warning");
                me.panel_infobox.select("div.status_text .dynamic")
                    .text("("+response.getMessage()+")");
                return;
            }

            var j,r,i,arr=[],idIndex=-1,itemId=0;
            var dataTable = response.getDataTable();
            var numCols = dataTable.getNumberOfColumns();

            // find the index with sheet.id (idIndex)
            for(i=0; true ; i++){
                if(i===numCols || dataTable.getColumnLabel(i).trim()===sheet.id) {
                    idIndex = i;
                    break;
                }
            }

            var tmpTable=[];

            // create the column name tables
            for(j=0; j<dataTable.getNumberOfColumns(); j++){
                tmpTable.push(dataTable.getColumnLabel(j).trim());
            }

            // create the item array
            arr.length = dataTable.getNumberOfRows(); // pre-allocate for speed
            for(r=0; r<dataTable.getNumberOfRows() ; r++){
                var c={};
                for(i=0; i<numCols ; i++) {
                    c[tmpTable[i]] = dataTable.getValue(r,i);
                }
                // push unique id as the last column if necessary
                if(c[sheet.id]===undefined) c[sheet.id] = itemId++;
                arr[r] = new kshf.Item(c,sheet.id);
            }

            me.finishDataLoad(sheet,arr);
        });
    },
    /** -- */
    loadSheet_CSV: function(sheet){
        var me=this;
        var fileName=this.source.dirPath+sheet.name+"."+this.source.fileType;
        $.ajax({
            url: fileName,
            type: "GET",
            async: (this.source.callback===undefined)?true:false,
            contentType: "text/csv",
            success: function(data) {
                // if data is already loaded, nothing else to do...
                if(kshf.dt[sheet.tableName]!==undefined){
                    me.incrementLoadedSheetCount();
                    return;
                }
                var arr = [];
                var idColumn = sheet.id;

                var config = {};
                config.dynamicTyping = true;
                config.header = true; // header setting can be turned off
                if(sheet.header===false) config.header = false;
                if(sheet.preview!==undefined) config.preview = sheet.preview;
                if(sheet.fastMode!==undefined) config.fastMode = sheet.fastMode;
                if(sheet.dynamicTyping!==undefined) config.dynamicTyping = sheet.dynamicTyping;

                var parsedData = Papa.parse(data, config);

                parsedData.data.forEach(function(row,i){
                    if(row[idColumn]===undefined) row[idColumn] = i;
                    arr.push(new kshf.Item(row,idColumn));
                })

                me.finishDataLoad(sheet, arr);
            }
        });
    },
    /** Note: Requires json root to be an array, and each object will be passed to keshif item. */
    loadSheet_JSON: function(sheet){
        var me=this;
        var fileName=this.source.dirPath+sheet.name+".json";
        $.ajax({
            url: fileName+"?dl=0",
            type: "GET",
            async: (this.source.callback===undefined)?true:false,
            dataType: "json",
            success: function(data) {
                // if data is already loaded, nothing else to do...
                if(kshf.dt[sheet.tableName]!==undefined){
                    me.incrementLoadedSheetCount();
                    return;
                }
                var arr = [];
                var idColumn = sheet.id;

                data.forEach(function(dataItem,i){
                    if(dataItem[idColumn]===undefined) dataItem[idColumn] = i;
                    arr.push(new kshf.Item(dataItem, idColumn));
                });

                me.finishDataLoad(sheet, arr);
            }
        });
    },
    /** -- */
    createTableFromTable: function(srcItems, dstTableName, summaryFunc){
        var i;
        var me=this;
        kshf.dt_id[dstTableName] = {};
        kshf.dt[dstTableName] = [];
        var dstTable_Id = kshf.dt_id[dstTableName];
        var dstTable = kshf.dt[dstTableName];

        var hasString = false;

        srcItems.forEach(function(srcData_i){
            var mapping = summaryFunc.call(srcData_i.data,srcData_i);
            if(mapping==="" || mapping===undefined || mapping===null) return;
            if(mapping instanceof Array) {
                mapping.forEach(function(v2){
                    if(v2==="" || v2===undefined || v2===null) return;
                    if(!dstTable_Id[v2]){
                        if(typeof(v2)==="string") hasString=true;
                        var itemData = {id: v2};
                        var item = new kshf.Item(itemData,'id');
                        dstTable_Id[v2] = item;
                        dstTable.push(item);
                    }
                });
            } else {
                if(!dstTable_Id[mapping]){
                    if(typeof(mapping)==="string") hasString=true;
                    var itemData = {id: mapping};
                    var item = new kshf.Item(itemData,'id');
                    dstTable_Id[mapping] = item;
                    dstTable.push(item);
                }
            }
        });

        // If any of the table values are string, convert all to string
        if(hasString){
            dstTable.forEach(function(item){
                item.data.id = ""+item.data.id;
            })
        }
    },
    /** -- */
    finishDataLoad: function(sheet,arr) {
        kshf.dt[sheet.name] = arr;
        var id_table = {};
        arr.forEach(function(r){id_table[r.id()] = r;});
        kshf.dt_id[sheet.tableName] = id_table;
        this.incrementLoadedSheetCount();
    },
    /** -- */
    incrementLoadedSheetCount: function(){
        var me=this;
        this.source.loadedTableCount++;
        this.panel_infobox.select("div.status_text .dynamic")
            .text("("+this.source.loadedTableCount+"/"+this.source.sheets.length+")");
            // finish loading
        if(this.source.loadedTableCount===this.source.sheets.length) {
            if(this.source.callback===undefined){
                this.loadCharts();
            } else {
                this.source.callback(this);
            }
        }
    },
    /** -- */
    loadCharts: function(){
        if(this.primaryTableName===undefined){
            alert("Cannot load keshif. Please define browser.primaryTableName.");
            return;
        }
        this.items = kshf.dt[this.primaryTableName];
        if(this.itemName==="") {
            this.itemName=this.primaryTableName;
        }

        var me=this;
        this.panel_infobox.select("div.status_text .info").text(kshf.lang.cur.CreatingBrowser);
        this.panel_infobox.select("div.status_text .dynamic").text("");
        window.setTimeout(function(){ me._loadCharts(); }, 50);
    },
    /** -- */
    _loadCharts: function(){
        var me=this;

        if(this.loadedCb!==undefined) this.loadedCb.call(this);

        // Total
        this.itemsTotal_Aggregrate_Total = 0;
        this.items.forEach(function(item){
            this.itemsTotal_Aggregrate_Total+=item.aggregate_Self;
        },this);

        // Create a summary for each existing column in the data
        for(var column in this.items[0].data){
            if(typeof(column)==="string") this.createSummary(column);
        }

        // Should do this here, because bottom panel width calls for browser width, and this reads the browser width...
        this.divWidth = this.domWidth();

        if(this.options.summaries) this.options.facets = this.options.summaries;
        this.options.facets = this.options.facets || [];

        this.options.facets.forEach(function(facetDescr){
            if(typeof facetDescr==="string"){
                facetDescr = {title: facetDescr};
            }
            if(facetDescr.sortingOpts){
                facetDescr.catSortBy = facetDescr.sortingOpts
            }
            if(facetDescr.catLabel||facetDescr.catTooltip||facetDescr.catTableName||facetDescr.catSortBy){
                facetDescr.type="categorical";
            } else if(facetDescr.intervalScale || facetDescr.showPercentile || facetDescr.unitName ){
                facetDescr.type="interval";
            }

            if(facetDescr.attribMap){
                facetDescr.value = facetDescr.attribMap;
            }

            var summary = this.summaries_by_name[facetDescr.title];
            if(summary===undefined){
                if(typeof(facetDescr.value)==="string"){
                    var summary = this.summaries_by_name[facetDescr.value];
                    if(summary===undefined){
                        summary = this.createSummary(facetDescr.value);
                    }
                    summary = this.changeSummaryName(facetDescr.value,facetDescr.title);
                } else if(typeof(facetDescr.value)==="function"){
                    summary = this.createSummary(facetDescr.title,facetDescr.value,facetDescr.type);
                } else{
                    return;
                }
            } else {
                if(facetDescr.value){
                    // Requesting a new summarywith the same name.
                    summary.destroy();
                    summary = this.createSummary(facetDescr.title,facetDescr.value,facetDescr.type);
                }
            }

            if(facetDescr.type){
                facetDescr.type = facetDescr.type.toLowerCase();
                if(facetDescr.type!==summary.type){
                    summary.destroy();
                    if(facetDescr.value===undefined){
                        facetDescr.value = facetDescr.title;
                    }
                    if(typeof(facetDescr.value)==="string"){
                        summary = this.createSummary(facetDescr.value,null,facetDescr.type);
                        if(facetDescr.value!==facetDescr.title)
                            this.changeSummaryName(facetDescr.value,facetDescr.title);
                    } else if(typeof(facetDescr.value)==="function"){
                        summary = this.createSummary(facetDescr.title,facetDescr.value,facetDescr.type);
                    }
                    // TODO!
                    // summary.updateSummaryDataType();
                }
            }
            if(summary===undefined){
                return;
            }

            summary.initializeAggregates();

            // Common settings
            if(facetDescr.collapsed){
                summary.setCollapsed(true);
            }
            if(facetDescr.items){
                summary.items = facetDescr.items;
            }
            if(facetDescr.description) summary.summaryDescription = facetDescr.description;

            // THESE AFFECT HOW CATEGORICAL VALUES ARE MAPPED
            if(summary.type==='categorical'){
                if(facetDescr.catTableName){
                    summary.setCatTable(facetDescr.catTableName);
                }
                if(facetDescr.catLabel){
                    summary.setCatLabel(facetDescr.catLabel);
                }
                if(facetDescr.catTooltip){
                    summary.setCatTooltip(facetDescr.catTooltip);
                }
                summary.catBarScale = facetDescr.catBarScale || summary.catBarScale;
                if(facetDescr.minAggrValue) summary.setMinAggrValue(facetDescr.minAggrValue);
                if(facetDescr.catSortBy!==undefined) summary.setSortingOpts(facetDescr.catSortBy);

                if(facetDescr.layout!=="none"){
                    facetDescr.layout = facetDescr.layout || 'left';
                    summary.addToPanel(this.panels[facetDescr.layout]);
                }
            }

            if(summary.type==='interval'){
                summary.unitName = facetDescr.unitName || summary.unitName;
                if(facetDescr.showPercentile){
                    summary.showPercentile = true;
                    summary.initDOM_Percentile();
                }
                summary.optimumTickWidth = facetDescr.optimumTickWidth || summary.optimumTickWidth;

                // add to panel before you set scale type and other options: TODO: Fix
                if(facetDescr.layout!=="none"){
                    facetDescr.layout = facetDescr.layout || 'left';
                    summary.addToPanel(this.panels[facetDescr.layout]);
                }

                if(facetDescr.intervalScale) {
                    summary.setScaleType(facetDescr.intervalScale);
                }
            }

            if(summary.isLinked) this.selfRefSummaries.push(summary);
        },this);

        this.panels.left.updateWidth_QueryPreview();
        this.panels.right.updateWidth_QueryPreview();
        this.panels.middle.updateWidth_QueryPreview();

        this.listDisplay = new kshf.RecordDisplay(this,this.listDef, this.DOM.root);

        this.setItemName();

        if(this.showDataSource !== false && this.source.url){
            this.DOM.datasource
                .style("display","inline-block")
                .attr("href",this.source.url);
        }

        this.checkZoomLevel();

        this.loaded = true;

        var x = function(){
            var totalWidth = this.divWidth;
            var colCount = 0;
            if(this.panels.left.summaries.length>0){
                totalWidth-=this.panels.left.width_catLabel+kshf.scrollWidth+this.panels.left.width_catMeasureLabel;
                colCount++;
            }
            if(this.panels.right.summaries.length>0){
                totalWidth-=this.panels.right.width_catLabel+kshf.scrollWidth+this.panels.right.width_catMeasureLabel;
                colCount++;
            }
            if(this.panels.middle.summaries.length>0){
                totalWidth-=this.panels.middle.width_catLabel+kshf.scrollWidth+this.panels.middle.width_catMeasureLabel;
                colCount++;
            }
            return Math.floor((totalWidth)/8);
        };
        var defaultBarChartWidth = x.call(this);

        this.panels.left.setWidthCatBars(this.options.barChartWidth || defaultBarChartWidth);
        this.panels.right.setWidthCatBars(this.options.barChartWidth || defaultBarChartWidth);
        this.panels.middle.setWidthCatBars(this.options.barChartWidth || defaultBarChartWidth);
        this.panels.bottom.updateSummariesWidth(this.options.barChartWidth || defaultBarChartWidth);

        this.updateMiddlePanelWidth();

        this.refresh_filterClearAll();

        this.items.forEach(function(item){item.updateWanted();});
        this.update_itemsWantedCount();

        this.updateAfterFilter();

        this.updateLayout_Height();

        // hide infobox
        this.panel_infobox.attr("show","none");

        this.insertAttributeList();

        if(this.readyCb!==undefined) this.readyCb(this);
        this.finalized = true;

        setTimeout(function(){
            me.setNoAnim(false);
        },10000);
    },
    /** -- */
    unregisterBodyCallbacks: function(){
        // TODO: Revert to previous handlers...
        d3.select("body").style('cursor','auto')
            .on("mousemove",null)
            .on("mouseup",null)
            .on("keydown",null);
    },
    /** -- */
    prepareDropZones: function(summary,source){
        this.movedSummary = summary;
        this.showDropZones = true;
        this.DOM.root
            .attr("showdropzone",true)
            .attr("dropattrtype",summary.getDataType())
            .attr("dropSource",source)
            ;
        this.DOM.attribDragBox.style("display","block").text(summary.summaryTitle);
        if(!summary.uniqueCategories()){
        }
    },
    /** -- */
    clearDropZones: function(){
        this.showDropZones = false;
        this.unregisterBodyCallbacks();
        this.DOM.root.attr("showdropzone",false);
        this.DOM.attribDragBox.style("display","none");
        if(this.movedSummary && !this.movedSummary.uniqueCategories()){
            // ?
        }
        this.movedSummary = undefined;
    },
    /** -- */
    setItemName: function(){
        this.DOM.recordName.html(this.itemName);
    },
    /** -- */
    insertAttributeList: function(){
        var me=this;
        var x=this.DOM.attributeList;

        var newAttributes = x.selectAll(".nugget")
            .data(this.summaries).enter();

        this.attribMoved = false;

        var newSummaries = newAttributes
            .append("div").attr("class","nugget editableTextContainer")
            .each(function(summary){
                summary.DOM.nugget = d3.select(this);
                summary.refreshNuggetDisplay();
            })
            .attr("title",function(summary){
                if(summary.summaryColumn!==undefined) return summary.summaryColumn;
            })
            .attr("state",function(summary){
                if(summary.summaryColumn===null) return "custom"; // calculated
                if(summary.summaryTitle===summary.summaryColumn) return "exact";
                return "edited";
            })
            .attr("datatype",function(summary){
                return summary.getDataType();
            })
            .attr("aggr_initialized",function(summary){
                return summary.aggr_initialized;
            })
            .on("dblclick",function(summary){
                if(summary.uniqueCategories()){
                    me.listDisplay.setRecordViewSummary(summary);
                    me.listDisplay.updateVisibleIndex();
                    me.listDisplay.updateItemVisibility(false,true);

                    if(me.listDisplay.textSearchSummary===null) 
                        me.listDisplay.setTextSearchSummary(summary);
                    return;
                }

                if(summary.hasTime!==undefined && summary.hasTime===true) {
                    summary.addToPanel(me.panels.bottom);
                } else if(summary.type==='categorical') {
                    summary.addToPanel(me.panels.left);
                    summary.refreshLabelWidth();
                    summary.updateBarPreviewScale2Active();
                } else if(summary.type==='interval') {
                    summary.addToPanel(me.panels.right);
                    me.listDisplay.addSortingOption(summary);
                }
                summary.refreshWidth();
                me.updateLayout();
            })
            .on("mousedown",function(summary){
                if(d3.event.which !== 1) return; // only respond to left-click

                var _this = this;
                me.attribMoved = false;
                d3.select("body")
                    .on("keydown", function(){
                        if(event.keyCode===27){ // Escape key
                            _this.removeAttribute("moved");
                            me.clearDropZones();
                        }
                    })
                    .on("mousemove", function(){
                        if(!me.attribMoved){
                            _this.setAttribute("moved","");
                            me.prepareDropZones(summary,"attributePanel");
                            me.attribMoved = true;
                        }
                        var mousePos = d3.mouse(me.DOM.root[0][0]);
                        kshf.Util.setTransform(me.DOM.attribDragBox[0][0],
                            "translate("+(mousePos[0]-20)+"px,"+(mousePos[1]+5)+"px)");
                        d3.event.stopPropagation();
                        d3.event.preventDefault();
                    })
                    .on("mouseup", function(){
                        if(!me.attribMoved) return;
                        _this.removeAttribute("moved");
                        me.DOM.root.attr("drag_cursor",null);
                        me.clearDropZones();
                        d3.event.preventDefault();
                    });
                d3.event.preventDefault();
            })
            .on("mouseup",function(summary){
                if(me.attribMoved===false) me.unregisterBodyCallbacks();
            })
            ;

        var nuggetViz = newSummaries.append("span").attr("class","nuggetViz")
            .each(function(summary){
                this.tipsy = new Tipsy(this, {
                    gravity: 'e', title: function(){
                        if(!summary.aggr_initialized){
                            return "Click to initialize";
                        }
                        return summary.getDataType();
                    }
                })
            })
            .on("mousedown",function(summary){
                if(!summary.aggr_initialized){
                    // stop dragging event start
                    d3.event.stopPropagation();
                    d3.event.preventDefault();
                }
            })
            .on("click",function(summary){
                if(!summary.aggr_initialized){
                    summary.initializeAggregates();
                }
            });

        nuggetViz.append("span").attr("class","nuggetInfo fa");
        var nuggetChart = nuggetViz.append("span").attr("class","nuggetChart");
        newSummaries.append("span").attr("class","summaryTitle editableText")
            .attr("contenteditable",false)
            .text(function(summary){ return summary.summaryTitle; })
            .on("blur",function(summary){
                this.parentNode.setAttribute("edittitle",false);
                this.setAttribute("contenteditable",false);
                me.changeSummaryName(summary.summaryTitle,this.textContent);
                d3.event.preventDefault();
                d3.event.stopPropagation();
            })
            .on("keydown",function(summary){
                if(d3.event.keyCode===13){ // ENTER
                    this.parentNode.setAttribute("edittitle",false);
                    this.setAttribute("contenteditable",false);
                    me.changeSummaryName(summary.summaryTitle,this.textContent);
                    d3.event.preventDefault();
                    d3.event.stopPropagation();
                }
            })
            ;
        newSummaries.append("div").attr("class","fa editTextButton")
            .each(function(summary){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){
                        var curState=this.parentNode.getAttribute("edittitle");
                        if(curState===null || curState==="false"){
                            return kshf.lang.cur.EditTitle;
                        } else {
                            return "OK";
                        }
                    }
                })
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("mousedown",function(summary){
                d3.event.stopPropagation();
                d3.event.preventDefault();
            })
            .on("click",function(summary){
                this.tipsy.hide();
                var parentDOM = d3.select(this.parentNode);
                var summaryTitle = parentDOM.select(".summaryTitle");
                var summaryTitle_DOM = parentDOM.select(".summaryTitle")[0][0];

                var curState=this.parentNode.getAttribute("edittitle");
                if(curState===null || curState==="false"){
                    this.parentNode.setAttribute("edittitle",true);
                    summaryTitle_DOM.setAttribute("contenteditable",true);
                    summaryTitle_DOM.focus();
                } else {
                    this.parentNode.setAttribute("edittitle",false);
                    summaryTitle_DOM.setAttribute("contenteditable",false);
                    me.changeSummaryName(summary.summaryTitle,summaryTitle_DOM.textContent);
                }
                // stop dragging event start
                d3.event.stopPropagation();
                d3.event.preventDefault();
            });

        newSummaries.append("div").attr("class","fa fa-code editCodeButton")
                .each(function(summary){
                    this.tipsy = new Tipsy(this, {
                        gravity: 'w', title: function(){ return "Edit Function"; }
                    });
                })
                .on("mouseenter",function(){ this.tipsy.show(); })
                .on("mouseleave",function(){ this.tipsy.hide(); })
                .on("mousedown",function(summary){
                    d3.event.stopPropagation();
                    d3.event.preventDefault();
                })
                .on("click",function(summary){
                    alert("TODO: Edit this:\n"+summary.getFuncString());
                    // stop dragging event start
                    d3.event.stopPropagation();
                    d3.event.preventDefault();
                })
                ;

        this.summaries.forEach(function(summary){
            if(summary.aggr_initialized) summary.refreshViz_Nugget();
        });
    },
    /** External method - used by demos to auto-select certain features on load -- */
    filterFacetAttribute: function(facetID, itemId){
        this.summaries[facetID].filterAttrib(this.summaries[facetID]._cats[itemId],"OR");
    },
    /** -- */
    clearFilters_All: function(force){
        var me=this;
        if(this.skipSortingFacet){
            // you can now sort the last filtered summary, attention is no longer there.
            this.skipSortingFacet.dirtySort = false;
            this.skipSortingFacet.DOM.root.attr("refreshSorting",false);
        }
        // clear all registered filters
        this.filters.forEach(function(filter){
            filter.clearFilter(false,false,false);
        })
        if(force!==false){
            this.items.forEach(function(item){ item.updateWanted_More(true); });
            this.update_itemsWantedCount();
            this.refresh_filterClearAll();
            this.updateAfterFilter(1); // more results
            if(sendLog){
                sendLog(kshf.LOG.FILTER_CLEAR_ALL);
            }
        }
        setTimeout( function(){ me.updateLayout_Height(); }, 1000); // update layout after 1.75 seconds
    },
    /** -- */
    refreshActiveItemCount: function(){
        var noneSelected = (this.itemsWanted_Aggregrate_Total===0);
        this.DOM.activeRecordCount
            .text(!noneSelected?this.itemsWanted_Aggregrate_Total:"No")
            .style("width",(noneSelected?"30":(this.itemsTotal_Aggregrate_Total.toString().length*11+5))+"px")
            ;
    },
    /** -- */
    update_itemsWantedCount: function(){
        this.itemsWantedCount = 0;
        this.itemsWanted_Aggregrate_Total = 0;
        this.items.forEach(function(item){
            if(item.isWanted){
                this.itemsWantedCount++;
                this.itemsWanted_Aggregrate_Total+=item.aggregate_Self;
            }
        },this);

        this.refreshTotalViz();
        this.refreshActiveItemCount();
    },
    /** @arg resultChange:
     * - If positive, more results are shown
     * - If negative, fewer results are shown
     * - Else, no info is available. */
    updateAfterFilter: function (resultChange) {
        this.clearPreviewCompare();
        // basically, propogate call under every facet and listDisplay
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.updateAfterFilter(resultChange);
        });
        this.listDisplay.updateAfterFilter();

        if(this.updateCb) this.updateCb(this);
    },
    /** -- */
    refresh_filterClearAll: function(){
        var filteredCount=0;
        this.filters.forEach(function(filter){ filteredCount+=filter.isFiltered?1:0; })
        this.DOM.root.attr("isfiltered",filteredCount>0);
    },
    /** Ratio mode is when glyphs scale to their max */
    setRatioMode: function(how){
        this.ratioModeActive = how;
        this.DOM.root.attr("ratiomode",how);
        this.setPercentMode(how);
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshViz_All();
        });
        if(this.ratioModeCb) this.ratioModeCb.call(this,!how);
    },
    /** -- */
    setPercentMode: function(how){
        this.percentModeActive = how;
        this.DOM.root.attr("percentview",how);
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshMeasureLabel();
        });
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshViz_Axis();
        });
    },
    /** -- */
    clearPreviewCompare: function(){
        this.vizCompareActive = false;
        this.DOM.root.attr("previewcompare",false);
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshViz_Compare();
        });
        if(this.comparedAggregate){
            this.comparedAggregate.DOM.facet.setAttribute("compare",false);
            this.comparedAggregate = null;
        }
        if(this.previewCompareCb) this.previewCompareCb.call(this,true);
    },
    /** -- */
    setPreviewCompare: function(aggregate){
        if(this.comparedAggregate){
            var a=aggregate===this.comparedAggregate;
            this.clearPreviewCompare();
            if(a) return;
        }
        aggregate.DOM.facet.setAttribute("compare",true);
        this.comparedAggregate = aggregate;
        this.vizCompareActive = true;
        this.DOM.root.attr("previewcompare",true);
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) {
                summary.cachePreviewValue();
                summary.refreshViz_Compare();
            }
        });
        if(this.previewCompareCb) this.previewCompareCb.call(this,false);
    },
    /** -- */
    clearResultPreviews: function(){
        this.vizPreviewActive = false;
        this.DOM.root.attr("resultpreview",false);
        this.items.forEach(function(item){
            item.updatePreview_Cache = false;
        });
        this.itemCount_Previewed = 0;
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.clearViz_Preview();
        });
        this.refreshTotalViz();
        if(this.previewCb) this.previewCb.call(this,true);
    },
    /** -- */
    refreshResultPreviews: function(){
        this.vizPreviewActive = true;
        this.DOM.root.attr("resultpreview",true);
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshViz_Preview();
        });
        this.refreshTotalViz();
        if(this.previewCb) this.previewCb.call(this,false);
    },
    /** -- */
    checkZoomLevel: function(){
        // Using devicePixelRatio works in Chrome and Firefox, but not in Safari
        // I have not tested IE yet.
        if(window.devicePixelRatio!==undefined){
            if(window.devicePixelRatio!==1 && window.devicePixelRatio!==2){
                var me=this;
                setTimeout(function(){
                    me.showWarning("Please reset your browser zoom level for the best experience.")
                },1000);
            } else {
                this.hideWarning();
            }
        } else {
            this.hideWarning();
        }
    },
    /** -- */
    updateLayout: function(){
        if(this.loaded!==true) return;
        this.checkZoomLevel();
        this.divWidth = this.domWidth();
        this.updateLayout_Height();
        this.updateMiddlePanelWidth();
    },
    /** -- */
    updateLayout_Height: function(){
        var me=this;
        var divHeight_Total = this.domHeight();

        var panel_Basic_height = Math.max(parseInt(this.DOM.panel_Basic.style("height")),24)+6;

        divHeight_Total-=panel_Basic_height;

        // initialize all summaries as not yet processed.
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.heightProcessed = false;
        })

        var bottomFacetsHeight=0;
        // process bottom summary too
        if(this.panels.bottom.summaries.length>0){
            var targetHeight=divHeight_Total/3;
            var maxHeight=0;
            // they all share the same target height
            this.panels.bottom.summaries.forEach(function(summary){
                targetHeight = Math.min(summary.getHeight_RangeMax(),targetHeight);
                summary.setHeight(targetHeight);
                summary.heightProcessed = true;
                bottomFacetsHeight += summary.getHeight();
            });
        }

        var doLayout = function(sectionHeight,summaries){
            var finalPass = false;
            var processedFacets=0;
            var lastRound = false;

            summaries.forEach(function(summary){
                // if it's already processed, log it
                if(summary.heightProcessed) processedFacets++;
            });

            while(true){
                var remainingFacetCount = summaries.length-processedFacets;
                if(remainingFacetCount===0) {
                    break;
                }
                var processedFacets_pre = processedFacets;
                summaries.forEach(function(summary){
                    // in last round, if you have more attribs than visible, you may increase your height!
                    if(lastRound===true && sectionHeight>5/*px*/ && !summary.collapsed && summary.catCount_Total!==undefined){
                        if(summary.catCount_InDisplay<summary.catCount_Total){
                            sectionHeight+=summary.getHeight();
                            summary.setHeight(sectionHeight);
                            sectionHeight-=summary.getHeight();
                            return;
                        }
                    }
                    if(summary.heightProcessed) return;
                    if(remainingFacetCount===0) return;
                    // auto-collapse summary if you do not have enough space
                    var targetHeight = Math.floor(sectionHeight/remainingFacetCount);
                    if(finalPass && targetHeight<summary.getHeight_RangeMin()){
                        summary.setCollapsed(true);
                    }
                    if(!summary.collapsed){
                        if(summary.getHeight_RangeMax()<=targetHeight){
                            // You have 10 rows available, but I need max 5. Thanks,
                            summary.setHeight(summary.getHeight_RangeMax());
                        } else if(finalPass){
                            summary.setHeight(targetHeight);
                        } else if(lastRound){
                        } else {
                            return;
                        }
                    }
                    sectionHeight-=summary.getHeight();
                    summary.heightProcessed = true;
                    processedFacets++;
                    remainingFacetCount--;
                },this);
                finalPass = processedFacets_pre===processedFacets;
                if(lastRound===true) break;
                if(remainingFacetCount===0) lastRound = true;
            }
            return sectionHeight;
        };

        var topPanelsHeight = divHeight_Total;
        if(this.panels.bottom.summaries.length>0) {
/*            if(this.showDropZones) {
                bottomFacetsHeight+=(1+this.panels.bottom.summaries.length)*36;
            }*/
        }
        this.panels.bottom.DOM.root.style("height",bottomFacetsHeight+"px");

        topPanelsHeight-=bottomFacetsHeight;
        this.DOM.panelsTop.style("height",topPanelsHeight+"px");

        // Left Panel
        if(this.panels.left.summaries.length>0){
            doLayout.call(this,topPanelsHeight,this.panels.left.summaries);
        }
        // Right Panel
        if(this.panels.right.summaries.length>0){
            doLayout.call(this,topPanelsHeight,this.panels.right.summaries);
        }
        // Middle Panel
        var midPanelHeight = 0;
        if(this.panels.middle.summaries.length>0){
            var panelHeight = topPanelsHeight;
            if(this.listDisplay.recordViewSummary){
                panelHeight -= 200; // give 200px fo the list display
            } else {
                panelHeight -= this.listDisplay.DOM.root[0][0].offsetHeight;
            }
            midPanelHeight = panelHeight - doLayout.call(this,panelHeight, this.panels.middle.summaries);
        }

        // The part where summary DOM is updated
        this.summaries.forEach(function(summary){
            if(summary.inBrowser()) summary.refreshHeight();
        });

        if(this.listDisplay){
            var listDivTop = 0;
            // get height of header
            var listHeaderHeight=this.listDisplay.DOM.recordViewHeader[0][0].offsetHeight;
            var listDisplayHeight = divHeight_Total-listDivTop-listHeaderHeight;
            if(this.panels.bottom.summaries.length>0){
                listDisplayHeight-=bottomFacetsHeight;
            }
            listDisplayHeight-=midPanelHeight;
            if(this.showDropZones && this.panels.middle.summaries.length===0) 
                listDisplayHeight*=0.5;
            if(this.listDisplay.recordViewSummary!==null)
                this.listDisplay.DOM.listItemGroup.style("height",listDisplayHeight+"px");
        }
    },
    /** -- */
    updateMiddlePanelWidth: function(){
        // for some reason, on page load, this variable may be null. urgh.
        var widthMiddlePanel = this.divWidth;
        var marginLeft = 0;
        var marginRight = 0;
        if(this.panels.left.summaries.length>0){
            marginLeft=2;
            widthMiddlePanel-=this.panels.left.getWidth_Total()+2;
        }
        if(this.panels.right.summaries.length>0){
            marginRight=2;
            widthMiddlePanel-=this.panels.right.getWidth_Total()+2;
        }
        this.panels.left.DOM.root.style("margin-right",marginLeft+"px")
        this.panels.right.DOM.root.style("margin-left",marginRight+"px")
        this.panels.middle.setTotalWidth(widthMiddlePanel);
        this.panels.middle.updateSummariesWidth();
        this.panels.bottom.setTotalWidth(this.divWidth);
        this.panels.bottom.updateSummariesWidth();
    },
    /** -- */
    getFilterState: function() {
        var r={
            resultCt : this.itemsWantedCount,
        };

        r.filtered="";
        r.selected="";
        this.filters.forEach(function(filter){
            if(filter.isFiltered){
                // set filtered to true for this summary ID
                if(r.filtered!=="") r.filtered+="x";
                r.filtered+=filter.id;
                // include filteing state of summary
                if(r.selected!=="") r.selected+="x";
            }
        },this);
        if(r.filtered==="") r.filtered=undefined;
        if(r.selected==="") r.selected=undefined;

        return r;
    },
    /** -- */
    getFilterSummary: function(){
        var str="";
        this.filters.forEach(function(filter,i){
            if(!filter.isFiltered) return;
            if(filter.filterView_Detail){
                if(i!=0) str+=" & ";
//                if(filter.summary_header) str+= filter.summary_header+": ";
                str+=filter.filterView_Detail();
            }
        },this);
        return str;
    }
};



// ***********************************************************************************************************
// ***********************************************************************************************************

kshf.Summary_Base = function(){}
kshf.Summary_Base.prototype = {
    initialize: function(browser,name,attribFunc){
        this.id = ++kshf.summaryCount;
        this.browser = browser;
//        this.parentFacet = options.parentFacet;

        this.summaryTitle   = name;
        this.summaryColumn = attribFunc?null:name;
        this.summaryFunc   = attribFunc || function(){ return this[name]; };

        this.chartScale_Measure = d3.scale.linear().clamp(true);

        this.DOM = {};
        this.DOM.inited = false;

        this.items = this.browser.items;
        if(this.items===undefined||this.items===null||this.items.length===0){
            alert("Error: Browser.items is not defined...");
            return;
        }

        this.subFacets = [];

        this.isRecordView = false;

        // Only used when summary is inserted into browser
        this.collapsed_pre = false;
        this.collapsed = false;

        this.aggr_initialized = false;

        this.createSummaryFilter();
    },
    /** -- */
    setSummaryName: function(name){
        this.summaryTitle = name;
        if(this.DOM.summaryTitle_text){
            this.DOM.summaryTitle_text.text(this.summaryTitle);
        }
        this.summaryFilter._refreshFilterSummary();
        // This summary may be used for sorting options. Refresh the list
        if(this.browser.listDisplay){
            this.browser.listDisplay.refreshSortingOptions();
        }
        if(this.isTextSearch){
            this.browser.listDisplay.DOM.recordTextSearch.select("input")
                .attr("placeholder",kshf.lang.cur.Search+": "+this.summaryTitle);
        }
        if(this.sortFunc){
            this.browser.listDisplay.refreshSortingOptions();
        }
        if(this.DOM.nugget){
            this.DOM.nugget.select(".summaryTitle").text(this.summaryTitle);
            this.DOM.nugget.attr("state",function(summary){
                if(summary.summaryColumn===null) return "custom"; // calculated
                if(summary.summaryTitle===summary.summaryColumn) return "exact";
                return "edited";
            });
        }
    },
    /** -- */
    getDataType: function(){
        if(this.type==='categorical') {
            var str="categorical";
            if(!this.aggr_initialized) return str+=" uninitialized";
            if(this.uniqueCategories()) str+=" unique";
            str+=this.hasMultiValueItem?" multivalue":" singlevalue";
            return str;
        }
        if(this.type==='interval') {
            if(!this.aggr_initialized) return str+=" uninitialized";
            if(this.hasTime) return "interval time";
            return "interval numeric";
            //
            if(this.hasFloat) return "floating";
            return "integer";
        }
        return "?";
    },
    /** -- */
    destroy: function(){
        delete this.browser.summaries_by_name[this.summaryTitle];
        if(this.summaryColumn)
            delete this.browser.summaries_by_name[this.summaryColumn];
        this.browser.removeSummary(this);
        if(this.DOM.root){
            this.DOM.root[0][0].parentNode.removeChild(this.DOM.root[0][0]);
        }
    },
    /** -- */
    inBrowser: function(){
        return this.panel!==undefined;
    },
    /** -- */
    hasEntityParent: function(){
        if(this.parentFacet===undefined) return false;
        return this.parentFacet.hasCategories();
    },
    /** -- */
    hasSubFacets: function(){
        return this.subFacets.length>0;
    },
    /** -- */
    clearDOM: function(){
        var dom = this.DOM.root[0][0];
        dom.parentNode.removeChild(dom);
    },
    /** -- */
    getWidth: function(){
        return this.panel.getWidth_Total()-this.getWidth_LeftOffset();
    },
    /** -- */
    getWidth_LeftOffset: function(){
        return (this.parentFacet)?17:0;
    },
    /** -- */
    uniqueCategories: function(){
        if(this.browser && this.browser.items[0].idIndex===this.summaryTitle){
            return true;
        }
        return false;
    },
    /** -- */
    isFiltered: function(){
        return this.summaryFilter.isFiltered;
    },
    getFuncString: function(){
        var str=this.summaryFunc.toString();
        // replace the beginning, and the end
        return str.replace(/function\s*\(\w*\)\s*{\s*/,"").replace(/}$/,"");
    },
    /** -- */
    addToPanel: function(panel, index){
        if(index===undefined) index = panel.summaries.length;
        if(this.panel===undefined){
            this.panel = panel;
        } else if(this.panel && this.panel!==panel){
            this.panel.removeSummary(this);
            this.panel = panel;
        } else{ // this.panel === panel
            var curIndex;
            // this.panel is the same as panel...
            this.panel.summaries.forEach(function(s,i){
                if(s===this) curIndex = i;
            },this);
            // inserting the summary to the same index as current one
            if(curIndex===index) return;
            var toRemove=this.panel.DOM.root.selectAll(".dropZone_between_wrapper")[0][curIndex];
            toRemove.parentNode.removeChild(toRemove);
        }
        var beforeDOM = this.panel.DOM.root.selectAll(".dropZone_between_wrapper")[0][index];
        if(this.DOM.root){
            this.DOM.root.style("display","");
            panel.DOM.root[0][0].insertBefore(this.DOM.root[0][0],beforeDOM);
        } else {
            this.initDOM(beforeDOM);
        }
        panel.addSummary(this,index);
        this.panel.refreshDropZoneIndex();
        this.refreshNuggetDisplay();
    },
    /** -- */
    refreshNuggetDisplay: function(){
        if(this.DOM.nugget===undefined) return;
        var me=this;
        var nuggetHidden = (this.panel||this.isRecordView);
        if(nuggetHidden){
            this.DOM.nugget.attr('anim','disappear');
            setTimeout(function(){
                me.DOM.nugget.style("display","none");
            },800);
        } else {
            this.DOM.nugget.style("display","block");
            setTimeout(function(){
                me.DOM.nugget.attr('anim','appear');
            },300);
        }
    },
    /** -- */
    removeFromPanel: function(){
        if(this.panel===undefined) return;
        this.panel.removeSummary(this);
        this.refreshNuggetDisplay();
    },
    /** -- */
    insertRoot: function(beforeDOM){
        this.DOM.root = this.panel.DOM.root.insert("div", function(){ return beforeDOM; });
        this.DOM.root
            .attr("class","kshfChart")
            .attr("chart_id",this.id)
            .attr("collapsed",this.collapsed)
            .attr("filtered",false);
    },
    /** -- */
    insertHeader: function(){
        var me = this;

        this.DOM.headerGroup = this.DOM.root.append("div").attr("class","headerGroup")
            .on("mousedown", function(){
                if(d3.event.which !== 1) return; // only respond to left-click
                if(!me.browser.attribsShown) {
                    d3.event.preventDefault();
                    return;
                }
                var _this = this;
                var _this_nextSibling = _this.parentNode.nextSibling;
                var _this_previousSibling = _this.parentNode.previousSibling;
                var moved = false;
                d3.select("body")
                    .style('cursor','move')
                    .on("keydown", function(){
                        if(event.keyCode===27){ // ESP key
                            _this.style.opacity = null;
                            me.browser.clearDropZones();
                        }
                    })
                    .on("mousemove", function(){
                        if(!moved){
                            _this_nextSibling.style.display = "none";
                            _this_previousSibling.style.display = "none";
                            _this.parentNode.style.opacity = 0.5;
                            me.browser.prepareDropZones(me,"browser");
                            moved = true;
                        }
                        var mousePos = d3.mouse(me.browser.DOM.root[0][0]);
                        kshf.Util.setTransform(me.browser.DOM.attribDragBox[0][0],
                            "translate("+(mousePos[0]-20)+"px,"+(mousePos[1]+5)+"px)");
                        d3.event.stopPropagation();
                        d3.event.preventDefault();
                    })
                    .on("mouseup", function(){
                        // Mouse up on the body
                        me.browser.clearDropZones();
                        if(me.panel!==undefined || true) {
                            _this.parentNode.style.opacity = null;
                            _this_nextSibling.style.display = "";
                            _this_previousSibling.style.display = "";
                        }
                        d3.event.preventDefault();
                    });
                d3.event.preventDefault();
            })
            ;

//        this.DOM.headerGroup.append("div").attr("class","border_line");

        var header_display_control = this.DOM.headerGroup.append("span").attr("class","header_display_control");

        header_display_control.append("span").attr("class","buttonSummaryCollapse fa fa-collapse")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: function(){ return me.panelOrder!==0?'sw':'nw'; },
                    title: function(){ return me.collapsed?kshf.lang.cur.OpenSummary:kshf.lang.cur.MinimizeSummary; }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                d3.event.preventDefault();
                d3.event.stopPropagation();
            })
            .on("click",function(){
                this.tipsy.hide();
                me.setCollapsedAndLayout(!me.collapsed); // flip
            })
            ;
        header_display_control.append("span").attr("class","buttonSummaryExpand fa fa-arrows-alt")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: function(){ return me.panelOrder!==0?'sw':'nw'; },
                    title: function(){ return kshf.lang.cur.MaximizeSummary; }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                d3.event.preventDefault();
                d3.event.stopPropagation();
            })
            .on("click",function(){
                me.panel.collapseAllSummaries();
                me.setCollapsedAndLayout(false); // uncollapse this one
            })
            ;
        header_display_control.append("span").attr("class","buttonSummaryRemove fa fa-remove")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: function(){ return me.panelOrder!==0?'sw':'nw'; },
                    title: function(){ return kshf.lang.cur.RemoveSummary; }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                d3.event.preventDefault();
                d3.event.stopPropagation();
            })
            .on("click",function(){
                // Clique control
                if(false){
                    me.parentFacet.show_cliques = !me.parentFacet.show_cliques;
                    me.parentFacet.DOM.root.attr("show_cliques",me.parentFacet.show_cliques);
                } else {
                    me.removeFromPanel();
                    me.clearDOM();
                    me.browser.updateLayout();
                }
            })
            ;

        this.DOM.summaryTitle = this.DOM.headerGroup.append("span")
            .attr("class","summaryTitle editableTextContainer")
            .attr("edittitle",false)
            .on("click",function(){ if(me.collapsed) me.setCollapsedAndLayout(false); })
            ;

        this.DOM.summaryTitle.append("span").attr("class","chartFilterButtonParent").append("div")
            .attr("class","chartClearFilterButton rowFilter alone")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: function(){ return me.panelOrder!==0?'s':'n'; },
                    title: function(){ return kshf.lang.cur.RemoveFilter; }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                d3.event.preventDefault();
                d3.event.stopPropagation();
            })
            .on("click", function(d,i){
                this.tipsy.hide();
                me.summaryFilter.clearFilter();
                if(sendLog) sendLog(kshf.LOG.FILTER_CLEAR_X, {id:me.summaryFilter.id});
            })
            .append("span").attr("class","fa fa-times")
            ;

        this.DOM.summaryTitle_text = this.DOM.summaryTitle.append("span").attr("class","summaryTitle_text editableText")
            .attr("contenteditable",false)
            .on("mousedown", function(){
                // stop dragging event start
                d3.event.stopPropagation();
            })
            .on("blur",function(){
                this.parentNode.setAttribute("edittitle",false);
                this.setAttribute("contenteditable", false);
                me.browser.changeSummaryName(me.summaryTitle,this.textContent);
            })
            .on("keydown",function(){
                if(event.keyCode===13){ // ENTER
                    this.parentNode.setAttribute("edittitle",false);
                    this.setAttribute("contenteditable", false);
                    me.browser.changeSummaryName(me.summaryTitle,this.textContent);
                }
            })
            .html((this.parentFacet && this.parentFacet.hasCategories())?
                ("<i class='fa fa-hand-o-up'></i> <span style='font-weight:500'>"+
                    this.parentFacet.summaryTitle+":</span> "+"  "+this.summaryTitle):
                this.summaryTitle
            );

        this.DOM.summaryTitle.append("span")
            .attr("class","editTextButton fa")
            .each(function(summary){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){
                        var curState=this.parentNode.getAttribute("edittitle");
                        if(curState===null || curState==="false"){
                            return kshf.lang.cur.EditTitle;
                        } else {
                            return "OK";
                        }
                    }
                })
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                // stop dragging event start
                d3.event.stopPropagation();
                d3.event.preventDefault();
            })
            .on("click",function(){
                var curState=this.parentNode.getAttribute("edittitle");
                if(curState===null || curState==="false"){
                    this.parentNode.setAttribute("edittitle",true);
                    var parentDOM = d3.select(this.parentNode);
                    var v=parentDOM.select(".summaryTitle_text")[0][0];
                    v.setAttribute("contenteditable",true);
                    v.focus();
                } else {
                    this.parentNode.setAttribute("edittitle",false);
                    var parentDOM = d3.select(this.parentNode);
                    var v=parentDOM.select(".summaryTitle_text")[0][0];
                    v.setAttribute("contenteditable",false);
                    me.browser.changeSummaryName(me.summaryTitle,v.textContent);
                }
            });

        this.DOM.facetIcons = this.DOM.headerGroup.append("span").attr("class","facetIcons");
        this.DOM.facetIcons.append("span").attr("class", "hasMultiMappings fa fa-tags")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: 'ne', title: function(){
                        return "Multiple "+me.summaryTitle+" possible.<br>Click to show relations.";
                    }
                });
            })
            .on("mouseover",function(d){
                this.tipsy.show();
            })
            .on("mouseout" ,function(d){
                this.tipsy.hide();
            })
            .on("click",function(d){
                me.show_cliques = !me.show_cliques;
                me.DOM.root.attr("show_cliques",me.show_cliques);
            })
            ;
//        this.DOM.headerGroup.append("div").attr("class","border_line border_line_bottom");

        this.setSummaryDescription(this.summaryDescription);
    },
    /** -- */
    setSummaryDescription: function(description){
        if(this.DOM.facetIcons===undefined) return;
        if(description===undefined) return;
        if(description===null) return;
        this.DOM.facetIcons.append("span").attr("class","summaryDescription fa fa-info-circle")
            .each(function(d){
                this.tipsy = new Tipsy(this, { gravity: 'ne', title: function(){ return description;} });
            })
            .on("mouseover",function(d){ this.tipsy.show(); })
            .on("mouseout" ,function(d){ this.tipsy.hide(); });
    },
    /** -- */
    insertChartAxis_Measure: function(dom, pos1, pos2){
        var me=this;
        this.DOM.chartAxis_Measure = dom.append("div").attr("class","chartAxis_Measure");
        this.DOM.chartAxis_Measure.append("span").attr("class","percentSign")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: pos1, title: function(){
                        return (me.browser.percentModeActive?"# "+kshf.lang.cur.Absolute:"% "+kshf.lang.cur.Percent)+
                            " <span class='fa fa-eye'></span>";
                    },
                })
            })
            .on("click",function(){
                me.browser.setPercentMode(!me.browser.percentModeActive);
                this.tipsy.hide();
            })
            .on("mouseover",function(){
                me.browser.DOM.root.selectAll(".percentSign").attr("highlight",true);
                this.tipsy.show();
                })
            .on("mouseout",function(){
                me.browser.DOM.root.selectAll(".percentSign").attr("highlight",false);
                this.tipsy.hide();
            });
        this.DOM.chartAxis_Measure.append("span").attr("class","chartAxis_Measure_background")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: pos2, title: function(){
                        return (me.browser.ratioModeActive?kshf.lang.cur.Absolute:kshf.lang.cur.Relative)+" "+
                            kshf.lang.cur.Width+
                            " <span class='fa fa-arrows-h'></span>";
                    },
                })
            })
            .on("click",function(){ me.browser.setRatioMode(!me.browser.ratioModeActive); })
            .on("mouseover",function(){
                me.browser.DOM.root.selectAll(".chartAxis_Measure_background").attr("highlight",true);
                this.tipsy.show();
            })
            .on("mouseout",function(){
                me.browser.DOM.root.selectAll(".chartAxis_Measure_background").attr("highlight",false);
                this.tipsy.hide();
            });
    },
    /** -- */
    setCollapsedAndLayout: function(hide){
        this.setCollapsed(hide);
        this.browser.updateLayout_Height();
        if(sendLog) sendLog( (hide===true?kshf.LOG.FACET_COLLAPSE:kshf.LOG.FACET_SHOW), {id:this.id} );
    },
    /** -- */
    unrollCollapsed: function(){
        this.setCollapsed(this.collapsed_pre);
    },
    /** -- */
    setCollapsed: function(v){
        this.collapsed_pre = this.collapsed;
        this.collapsed = v;
        if(this.DOM.root){
            this.DOM.root.attr("collapsed",this.collapsed);
            if(!this.collapsed) {
                this.clearViz_Preview();
                this.refreshViz_All();
            } else {
                this.DOM.headerGroup.select(".buttonSummaryExpand").style("display","none");
            }
        }
        return this; // allow chaining
    },
};

kshf.Summary_Categorical = function(){};
kshf.Summary_Categorical.prototype = new kshf.Summary_Base();
var Summary_Categorical_functions = {
    /** -- */
    initialize: function(browser,name,attribFunc){
        kshf.Summary_Base.prototype.initialize.call(this,browser,name,attribFunc);
        this.type='categorical';

        this.heightRow_category = 18;

        this.show_cliques = false;

        this.scrollTop_cache=0;
        this.cat_InDisplay_First = 0;
        this.configRowCount=0;

        // These settings affect the categories
        this.minAggrValue=1;
        this.removeInactiveCats = true;

        this.catSortBy = [];

        this.isLinked = false; // TODO: document / update

        this.setCatLabel("id");

        if(this.items.length<=1000) this.initializeAggregates();
    },
    /** -- */
    initializeAggregates: function(){
        if(this.aggr_initialized) return;
        if(this.catTableName===undefined){
            this.catTableName = this.summaryTitle+"_h_"+this.id;
            this.browser.createTableFromTable(this.items, this.catTableName, this.summaryFunc);
        }
        if(kshf.dt[this.catTableName]===undefined){
            return false; // Cannot initialize, table not defined.
        }
        this.mapToAggregates();
        if(this.catSortBy.length===0) this.setSortingOpts();
        if(this.getMaxAggr_Total()!=1 && this._cats.length>1) this.sortCategories();

        this.aggr_initialized = true;
        this.refreshViz_Nugget();
    },
    /** -- */
    refreshViz_Nugget: function(){
        if(this.DOM.nugget===undefined) return;
        var nuggetChart = this.DOM.nugget.select(".nuggetChart");

        this.DOM.nugget
            .attr("aggr_initialized",this.aggr_initialized)
            .attr("datatype",this.getDataType());

        if(!this.aggr_initialized) return;

        if(this.uniqueCategories()){
            this.DOM.nugget.select(".nuggetInfo").html("<span class='fa fa-tag'></span><br>Unique");
            nuggetChart.style("display",'none');
            return;
        }

        var totalWidth= 25;
        var maxAggregate_Total = this.getMaxAggr_Total();
        nuggetChart.selectAll(".nuggetBar").data(this._cats).enter()
            .append("span").attr("class","nuggetBar")
                .style("width",function(cat){ return totalWidth*(cat.items.length/maxAggregate_Total)+"px"; });

        this.DOM.nugget.select(".nuggetInfo").html(
            "<span class='fa fa-tag"+(this.hasMultiValueItem?"s":"")+"'></span><br>"+
            this._cats.length+"<br>rows<br>");
    },
    /** -- */
    getHeight: function(){
        if(!this.hasCategories() || this.collapsed) return this.getHeight_Header();
        return this.getHeight_Header() + this.getHeight_Content();
    },
    /** -- */
    getHeight_Header: function(){
        if(this._height_header==undefined) {
            this._height_header = this.DOM.headerGroup[0][0].offsetHeight;
            if(this.hasSubFacets()){
                this._height_header+=2;
            }
        }
        return this._height_header;
    },
    /** -- */
    getHeight_RangeMax: function(){
        if(!this.hasCategories()) return this.heightRow_category;
        return this.getHeight_Header()+(this.configRowCount+this.catCount_Visible+1)*this.heightRow_category-1;
    },
    /** -- */
    getHeight_RangeMin: function(){
        if(!this.hasCategories()) return this.getHeight_Header();
        return this.getHeight_Header()+this.getHeight_Config()+(Math.min(this.catCount_Visible,2)+1)*this.heightRow_category;
    },
    /** -- */
    getHeight_Config: function(){
        var r=0;
        if(this.configRowCount!=0) r+=1; // bottom border : 1 px
        if(this.showTextSearch) r+=18;
        if(this.catSortBy.length>1) r+=17;
        return r;
    },
    /** -- */
    getHeight_Bottom: function(){
        if(!this.areAllCatsInDisplay() || !this.panel.hideBarAxis || this.catCount_Total>4) return 18;
        return 0;
    },
    /** -- */
    getHeight_Content: function(){
        return this.attribHeight + this.getHeight_Config() + this.getHeight_Bottom();
    },
    /** -- */
    getWidth_Label: function(){
        return this.panel.width_catLabel-this.getWidth_LeftOffset();
    },
    /** -- */
    areAllCatsInDisplay: function(){
        return this.catCount_Visible===this.catCount_InDisplay;
    },
    /** -- */
    hasCategories: function(){
        if(this._cats && this._cats.length===0) return false;
        return this.summaryFunc!==undefined;
    },
    /** -- */
    uniqueCategories: function(){
        return this.getMaxAggr_Total()===1;
    },
    /** -- */
    insertSortingOption: function(opt){
        this.catSortBy.push( this.prepareSortingOption(opt) );
    },
    /** -- */
    prepareSortingOption: function(opt){
        opt.inverse = opt.inverse || false; // Default is false
        if(opt.value){
            if(typeof(opt.value)==="string"){
                opt.name = x;
                var x = opt.value;
                opt.value = function(){ return this[x]; }
            } else if(typeof(opt.value)==="function"){
                if(opt.name===undefined) opt.name = "custom"
            }
            if(opt.no_resort===undefined) opt.no_resort = true;
        } else {
            opt.name = opt.name || "# of Active";
        }
        if(opt.no_resort===undefined) opt.no_resort = (this.catCount_Total<=4);
        return opt;
    },
    /** -- */
    setSortingOpts: function(opts){
        this.catSortBy = opts || {};
        if(!Array.isArray(this.catSortBy)){
            this.catSortBy = [this.catSortBy];
        }

        this.catSortBy.forEach(function(opt,i){
            if(typeof opt==="string" || typeof opt==="function"){
                this.catSortBy[i] = {value: opt};
            }
        },this);

        this.catSortBy.forEach(function(opt){
            this.prepareSortingOption(opt);
        },this);

        this.catSortBy_Active = this.catSortBy[0];

        this.updateCatSorting(0,true,true);
        this.refreshSortOptions();
        this.refreshSortButton();
    },
    /** -- */
    setCatLabel: function( catLabel ){
        if(typeof(catLabel)==="function"){
            this.catLabel = catLabel;
        } else if(typeof(catLabel)==="string" || typeof(catLabel)=="number"){
            var x = catLabel;
            this.catLabel = function(){ return this[x]; };
        } else {
            return;
        }
        var me=this;
        if(this.DOM.theLabel)
            this.DOM.theLabel.html(function(cat){ return me.catLabel.call(cat.data); });
    },
    /** -- */
    setCatTooltip: function( catTooltip ){
        if(typeof(catTooltip)==="function"){
            this.catTooltip = catTooltip;
        } else if(typeof(catTooltip)==="string"){
            var x = catTooltip;
            this.catTooltip = function(){ return this[x]; };
        } else {
            return;
        }
        if(this.DOM.cats)
            this.DOM.cats.attr("title",function(cat){ return me.catTooltip.call(cat.data); });
    },
    /** -- */
    setCatTable: function(tableName){
        this.catTableName = tableName;
        if(tableName===""){
            this.catTableName = this.summaryTitle+"_h_"+this.id;
        } else {
            if(this.catTableName===this.browser.primaryTableName){
                this.isLinked=true;
                //this.browser.listDef.hasLinkedItems = true;
                this.catTableName = this.summaryTitle+"_h_"+this.id;
                kshf.dt_id[this.catTableName] = kshf.dt_id[this.browser.primaryTableName];
                kshf.dt[this.catTableName] = this.items.slice();
            }
        }
        if(this.aggr_initialized){
            this.mapToAggregates();
            this.updateCats();
        }
    },
    /** -- */
    createSummaryFilter: function(){
        var me=this;
        this.summaryFilter = this.browser.createFilter({
            parentSummary: this,
            onClear: function(summary){
                summary.clearCatTextSearch();
                summary.unselectAllAttribs();
                summary._update_Selected();
            },
            onFilter: function(summary){
                // at least one category is selected in some modality (and/ or/ not)
                summary._update_Selected();

                var filterId = this.id;

                summary.items.forEach(function(item){
                    var recordVal_s=item.mappedDataCache[filterId];

                    if(recordVal_s===null){
                        // survives if AND and OR is not selected
                        item.setFilterCache(filterId, this.selected_AND.length===0 && this.selected_OR.length===0 );
                        return;
                    }

                    // Check NOT selections - If any mapped item is NOT, return false
                    // Note: no other filtering depends on NOT state.
                    // This is for ,multi-level filtering using not query
        /*            if(this.selected_NOT.length>0){
                        if(!recordVal_s.every(function(item){
                            return !item.is_NOT() && item.isWanted;
                        })){
                            item.setFilterCache(filterId,false); return;
                        }
                    }*/

                    // If any of the record values are selected with NOT, the item will be removed
                    if(this.selected_NOT.length>0){
                        if(!recordVal_s.every(function(val){ return !val.is_NOT(); })){
                            item.setFilterCache(filterId,false); return;
                        }
                    }
                    // All AND selections must be among the record values
                    if(this.selected_AND.length>0){
                        // Compute the number of record values selected with AND.
                        var t=0;
                        recordVal_s.forEach(function(m){ if(m.is_AND()) t++; })
                        if(t!==this.selected_AND.length){
                            item.setFilterCache(filterId,false); return;
                        }
                    }
                    // One of the OR selections must be among the item values
                    // Check OR selections - If any mapped item is OR, return true
                    if(this.selected_OR.length>0){
                        item.setFilterCache(filterId, recordVal_s.some(function(d){return (d.is_OR());}) );
                        return;
                    }
                    // only NOT selection
                    item.setFilterCache(filterId,true);
                }, this);
            },
            filterView_Detail: function(){
                // 'this' is the Filter
                // go over all items and prepare the list
                var selectedItemsText="";
                var catTooltip = me.catTooltip;

                var totalSelectionCount = this.selectedCount_Total();

                if(me.subFacets.some(function(summary){ return summary.isFiltered();})){
                    return " <i class='fa fa-hand-o-right'></i>";;
                }

                var query_and = " <span class='AndOrNot AndOrNot_And'>"+kshf.lang.cur.And+"</span> ";
                var query_or = " <span class='AndOrNot AndOrNot_Or'>"+kshf.lang.cur.Or+"</span> ";
                var query_not = " <span class='AndOrNot AndOrNot_Not'>"+kshf.lang.cur.Not+"</span> ";

                if(totalSelectionCount>4 || this.linkFilterSummary){
                    selectedItemsText = "<b>"+totalSelectionCount+"</b> selected";
                    // Note: Using selected because selections can include not, or,and etc (a variety of things)
                } else {
                    var selectedItemsCount=0;

                    // OR selections
                    if(this.selected_OR.length>0){
                        var useBracket_or = this.selected_AND.length>0 || this.selected_NOT.length>0;
                        if(useBracket_or) selectedItemsText+="[";
                        // X or Y or ....
                        this.selected_OR.forEach(function(attrib,i){
                            selectedItemsText+=((i!==0 || selectedItemsCount>0)?query_or:"")+"<span class='attribName'>"
                                +me.catLabel.call(attrib.data)+"</span>";
                            selectedItemsCount++;
                        });
                        if(useBracket_or) selectedItemsText+="]";
                    }
                    // AND selections
                    this.selected_AND.forEach(function(attrib,i){
                        selectedItemsText+=((selectedItemsText!=="")?query_and:"")
                            +"<span class='attribName'>"+me.catLabel.call(attrib.data)+"</span>";
                        selectedItemsCount++;
                    });
                    // NOT selections
                    this.selected_NOT.forEach(function(attrib,i){
                        selectedItemsText+=query_not+"<span class='attribName'>"+me.catLabel.call(attrib.data)+"</span>";
                        selectedItemsCount++;
                    });
                }
                if(this.linkFilterSummary){
                    selectedItemsText+= "<i class='fa fa-hand-o-left'></i><br> ["+this.linkFilterSummary+"]";
                }

                return selectedItemsText;
            }
        });

        this.summaryFilter.selected_AND = [];
        this.summaryFilter.selected_OR = [];
        this.summaryFilter.selected_NOT = [];
        this.summaryFilter.selectedCount_Total = function(){
            return this.selected_AND.length + this.selected_OR.length + this.selected_NOT.length;
        };
        this.summaryFilter.selected_Any = function(){
            return this.selected_AND.length>0 || this.selected_OR.length>0 || this.selected_NOT.length>0;
        };
        this.summaryFilter.selected_All_clear = function(){
            kshf.Util.clearArray(this.selected_AND);
            kshf.Util.clearArray(this.selected_OR);
            kshf.Util.clearArray(this.selected_NOT);
        };
    },
    /** -- */
    insertSubFacets: function(){
        this.DOM.subFacets=this.DOM.root.append("div").attr("class","subFacets");

        this.DOM.subFacets.append("span").attr("class","facetGroupBar").append("span").attr("class","facetGroupBarSub");

        if(!this.hasCategories()){
            this.options.facets.forEach(function(facetDescr){
                facetDescr.parentFacet = this;
                facetDescr.panel = this.panel;
                var fct=this.browser.addFacet(facetDescr,this.browser.primaryTableName);
                this.subFacets.push(fct);
            },this);
        } else {
            this.options.facets.forEach(function(facetDescr){
                facetDescr.parentFacet = this;
                facetDescr.panel = this.panel;
                facetDescr.items = this._cats;
                var fct=this.browser.addFacet(facetDescr,this.catTableName);
                this.subFacets.push(fct);
            },this);
        }

        // Init facet DOMs after all facets are added / data mappings are completed
        this.subFacets.forEach(function(summary){ summary.initDOM(); });
    },
    /** --
     * Note: accesses summaryFilter, summaryFunc
     */
    mapToAggregates: function(){
        var filterId = this.summaryFilter.id, me=this;

        var targetTable_id = {};
        var targetTable = [];
        kshf.dt[this.catTableName].forEach(function(srcI){
            var i = new kshf.Item(srcI.data,srcI.idIndex);
            targetTable_id[i.id()] = i;
            targetTable.push(i);
        });
        this.catTable = targetTable;
        var maxDegree = 0;
        this.items.forEach(function(item){
            item.mappedDataCache[filterId] = null; // default mapping to null

            var mapping = this.summaryFunc.call(item.data,item);
            if(mapping===undefined || mapping==="" || mapping===null)
                return;
            if(mapping instanceof Array){
                var found = {};
                mapping = mapping.filter(function(e){
                    if(e===undefined || e==="" || e===null) return false; // remove invalid values
                    if(found[e]===undefined){ found[e] = true;  return true; } // remove duplicate values
                    return false;
                });
                if(mapping.length===0) return; // empty array - checked after removing invalid/duplicates
            } else {
                mapping = [mapping];
            }
            maxDegree = Math.max(maxDegree, mapping.length);

            item.mappedDataCache[filterId] = [];
            mapping.forEach(function(a){
                var m=targetTable_id[a];
                if(m==undefined) return;
                item.mappedDataCache[filterId].push(m);
                m.addItem(item);
            });
        }, this);

        this.hasMultiValueItem = maxDegree>1;

        // TODO: Fix!!!!
        // add degree filter if attrib has multi-value items and set-vis is enabled
        if(this.hasMultiValueItem && this.enableSetVis){
            var fscale;
            if(maxDegree>100) fscale = 'log';
            else if(maxDegree>10) fscale = 'linear';
            else fscale = 'step';
            // TODO: FIX!!!
            var facetDescr = {
                title:"<i class='fa fa-hand-o-up'></i> # of "+this.summaryTitle,
                value: function(d){
                    var arr=d.mappedDataCache[filterId];
                    if(arr==null) return 0;
                    return arr.length;
                },
                parentFacet: this.parentFacet,
                collapsed: true,
                type: 'interval',
                intervalScale: fscale,
                layout: this.panel
            };
            this.browser.addFacet(facetDescr,this.browser.primaryTableName);
        }

        this.updateCats();

        this.unselectAllAttribs();
    },
    // TODO: Check how isLinked and dataMap (old variable) affected this calculations...
    // Modified internal dataMap function - Skip rows with 0 active item count
    setMinAggrValue: function(v){
        this.minAggrValue = Math.max(1,v);
        this.updateCats();
    },
    /** -- */
    updateCats: function(){
        this._cats = this.catTable.filter(function(cat){
            return cat.items.length>=this.minAggrValue;
        },this);
        this.updateCatCount_Total();
        this.updateCatCount_Visible();
    },
    /** -- */
    updateCatCount_Total: function(){
        this.catCount_Total = this._cats.length;
        this.catCount_Wanted = this.catCount_Total;
        if(this.catCount_Total===1){
            this.catBarScale = "scale_frequency";
        }
        if(this.catCount_Total<=4) {
            this.catSortBy.forEach(function(opt){ opt.no_resort=true; });
        }
        this.showTextSearch = this.catCount_Total>=20;
    },
    /** -- */
    updateCatCount_Wanted: function(){
        this.catCount_Wanted = 0;
        this._cats.forEach(function(cat){ if(cat.isWanted) this.catCount_Wanted++; },this);
    },
    /** -- */
    updateCatCount_Visible: function(){
        this.catCount_Visible = 0;
        this.catCount_NowVisible = 0;
        this.catCount_NowInvisible = 0;
        this._cats.forEach(function(cat){
            v = this.isAttribVisible(cat);
            cat.isVisible_before = cat.isVisible;
            cat.isVisible = v;
            if(!cat.isVisible && cat.isVisible_before) this.catCount_NowInvisible++;
            if(cat.isVisible && !cat.isVisible_before) this.catCount_NowVisible++;
            if(cat.isVisible) this.catCount_Visible++;
        },this);
    },
    /** -- */
    initDOM: function(beforeDOM){
        this.initializeAggregates();

        if(this.DOM.inited===true) return;
        var me = this;

        this.insertRoot(beforeDOM);

        this.DOM.root
            .attr("filtered_or",0)
            .attr("filtered_and",0)
            .attr("filtered_not",0)
            .attr("filtered_total",0)
            .attr("hasMultiValueItem",this.hasMultiValueItem)
            .attr("refreshSorting",false)
            ;

        this.insertHeader();

        if(this.hasCategories()) this.init_DOM_Cat();

        // TODO: Insert subfacets here
        if(this.facets){
            this.DOM.root.attr("hasFacets",true);
            this.insertSubFacets();
            // no-attrib facets (hierarchy parents) still need to adjust their header position
            this.refreshLabelWidth();
        }

        this.setCollapsed(this.collapsed);

        this.DOM.inited = true;
    },
    /** -- */
    refreshConfigRowCount: function(){
        this.configRowCount = 0;
        if(this.showTextSearch){
            this.configRowCount++;
        }
        if(this.catSortBy.length>1) {
            this.configRowCount++;
        }
        if(this.configRowCount>0){
            this.DOM.facetControls.style("display","block");
        }
    },
    /** -- */
    init_DOM_Cat: function(){
        var me=this;
        this.DOM.wrapper = this.DOM.root.append("div").attr("class","wrapper");

        this.DOM.facetCategorical = this.DOM.wrapper.append("div").attr("class","facetCategorical")
            ;

        // create config row(s) if needed
        this.DOM.facetControls = this.DOM.facetCategorical.append("div").attr("class","facetControls");
        this.initDOM_CatTextSearch();
        this.initDOM_CatSortButton();
        this.initDOM_CatSortOpts();

        if(this.showTextSearch){
            this.DOM.attribTextSearch.style("display","block");
        }
        this.refreshConfigRowCount();

        this.DOM.scrollToTop = this.DOM.facetCategorical.append("div").attr("class","scrollToTop fa fa-arrow-up")
            .each(function(){
                this.tipsy = new Tipsy(this, {gravity: 'e', title: function(){ return kshf.lang.cur.ScrollToTop; }});
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("click",function(d){
                this.tipsy.hide();
                kshf.Util.scrollToPos_do(me.DOM.attribGroup[0][0],0);
                if(sendLog) sendLog(kshf.LOG.FACET_SCROLL_TOP, {id:me.id} );
            })
            ;

        this.DOM.attribGroup = this.DOM.facetCategorical.append("div").attr("class","attribGroup")
            .on("mousedown",function(){
                d3.event.stopPropagation();
                d3.event.preventDefault();
            })
            .on("scroll",function(d){
                if(kshf.Util.ignoreScrollEvents===true) return;
                me.scrollTop_cache = me.DOM.attribGroup[0][0].scrollTop;

                me.DOM.scrollToTop.style("visibility", me.scrollTop_cache>0?"visible":"hidden");

                me.cat_InDisplay_First = Math.floor(me.scrollTop_cache/me.heightRow_category);
                me.refreshScrollDisplayMore(me.cat_InDisplay_First+me.catCount_InDisplay);
                me.updateAttribCull();
                me.cullAttribs();
                me.refreshMeasureLabel();

                me.browser.pauseResultPreview = true;
                if(this.pauseTimer) clearTimeout(this.pauseTimer);
                this.pauseTimer = setTimeout(function(){me.browser.pauseResultPreview=false;}, 200);
            });
        // with this, I make sure that the (scrollable) div height is correctly set to visible number of categories
        this.DOM.chartBackground = this.DOM.attribGroup.append("span").attr("class","chartBackground");

        this.DOM.chartCatLabelResize = this.DOM.attribGroup.append("span").attr("class","chartCatLabelResize dragWidthHandle")
            .on("mousedown", function (d, i) {
                var resizeDOM = this;
                me.panel.DOM.root.attr("catLabelDragging",true);

                me.browser.DOM.pointerBlock.attr("active","");
                me.browser.DOM.root.style('cursor','col-resize');
                me.browser.setNoAnim(true);
                var mouseDown_x = d3.mouse(d3.select("body")[0][0])[0];
                var initWidth = me.panel.width_catLabel;

                d3.select("body").on("mousemove", function() {
                    var mouseDown_x_diff = d3.mouse(d3.select("body")[0][0])[0]-mouseDown_x;
                    me.panel.setWidthCatLabel(initWidth+mouseDown_x_diff);
                }).on("mouseup", function(){
                    me.panel.DOM.root.attr("catLabelDragging",false);
                    me.browser.DOM.pointerBlock.attr("active",null);
                    me.browser.DOM.root.style('cursor','default');
                    me.browser.setNoAnim(false);
                    d3.select("body").on("mousemove", null).on("mouseup", null);
                });
               d3.event.preventDefault();
           });

        this.DOM.belowAttribs = this.DOM.facetCategorical.append("div").attr("class","belowAttribs");
        this.DOM.belowAttribs.append("div").attr("class", "border_line");

        this.insertChartAxis_Measure(this.DOM.belowAttribs,'e','e');

        this.DOM.scroll_display_more = this.DOM.belowAttribs.append("div").attr("class","hasLabelWidth")
            .append("span").attr("class","scroll_display_more")
            .on("click",function(){
                kshf.Util.scrollToPos_do(
                    me.DOM.attribGroup[0][0],me.DOM.attribGroup[0][0].scrollTop+me.heightRow_category);
                if(sendLog) sendLog(kshf.LOG.FACET_SCROLL_MORE, {id:me.id});
            });

        this.insertCategories();

        this.refreshLabelWidth();

        this.updateCatSorting(0,true,true);
    },
    /** -- */
    initDOM_CatSortButton: function(){
        var me=this;
        this.DOM.catSortButton = this.DOM.facetControls.append("span").attr("class","catSortButton sortButton fa")
            .on("click",function(d){
                if(me.dirtySort){
                    me.dirtySort = false;
                    me.DOM.root.attr("refreshSorting",false);
                } else{
                    me.catSortBy_Active.inverse = me.catSortBy_Active.inverse?false:true;
                    me.refreshSortButton();
                }
                me.updateCatSorting(0,true);
            })
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){
                        return me.dirtySort?kshf.lang.cur.Reorder:kshf.lang.cur.ReverseOrder;
                    }
                })
            })
            .on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); });
        this.refreshSortButton();
    },
    /** -- */
    initDOM_CatSortOpts: function(){
        var me=this;
        var x = this.DOM.facetControls.append("span").attr("class","sortOptionSelectGroup hasLabelWidth");

        this.DOM.optionSelect = x.append("select").attr("class","optionSelect")
            .on("change", function(){
                me.catSortBy_Active = me.catSortBy[this.selectedIndex];
                me.refreshSortButton();
                me.updateCatSorting(0,true);
                if(sendLog) sendLog(kshf.LOG.FACET_SORT, {id:me.id, info:this.selectedIndex});
            })

        this.refreshSortOptions();
    },
    /** -- */
    refreshSortButton: function(){
        if(this.DOM.catSortButton===undefined) return;
        this.DOM.catSortButton
            //.style("display",(this.catSortBy_Active.no_resort?"none":"inline-block"))
            .style("display","inline-block")
            .attr("inverse",this.catSortBy_Active.inverse);
    },
    /** -- */
    refreshSortOptions: function(){
        if(this.DOM.optionSelect===undefined) return;

        this.refreshConfigRowCount();

        this.DOM.optionSelect.style("display", (this.catSortBy.length>1)?"block":"none" );

        this.DOM.optionSelect.selectAll(".sort_label").data([]).exit().remove(); // remove all existing options

        var x= this.DOM.optionSelect.selectAll(".sort_label")
            .data(this.catSortBy)
            .enter().append("option").attr("class", "sort_label").text(function(d){ return d.name; });
    },
    /** -- */
    initDOM_CatTextSearch: function(){
        var me=this;
        this.DOM.attribTextSearch = this.DOM.facetControls.append("div").attr("class","attribTextSearch hasLabelWidth");
        this.DOM.attribTextSearchControl = this.DOM.attribTextSearch.append("span")
            .attr("class","attribTextSearchControl fa")
            .on("click",function() { me.summaryFilter.clearFilter(); });
        this.DOM.attribTextSearchInput = this.DOM.attribTextSearch.append("input")
            .attr("class","attribTextSearchInput")
            .attr("type","text")
            .attr("placeholder",kshf.lang.cur.Search)
//            .on("mousedown",function(){alert('sdsdd');})
            .on("input",function(){
                if(this.timer){
                    clearTimeout(this.timer);
                }
                var x = this;
                this.timer = setTimeout( function(){
                    var v=x.value.toLowerCase();
                    if(v===""){
                        me.summaryFilter.clearFilter();
                    } else {
                        me.DOM.attribTextSearchControl.attr("showClear",true);
                        me.summaryFilter.selected_All_clear();
                        me._cats.forEach(function(attrib){
                            if(me.catLabel.call(attrib.data).toString().toLowerCase().indexOf(v)!==-1){
                                attrib.set_OR(me.summaryFilter.selected_OR);
                            } else {
                                // search in tooltiptext
                                if(me.catTooltip){
                                    var tooltipText = me.catTooltip.call(attrib.data);
                                    if(tooltipText && tooltipText.toLowerCase().indexOf(v)!==-1) {
                                        attrib.set_OR(me.summaryFilter.selected_OR);
                                    }
                                } else{
                                    attrib.set_NONE();
                                }
                            }
                        });
                        if(me.summaryFilter.selectedCount_Total()===0){
                            me.summaryFilter.clearFilter();
                        } else {
                            me.summaryFilter.how = "All";
                            me.summaryFilter.addFilter(true);
                            me.summaryFilter.linkFilterSummary = "";
                            if(sendLog) sendLog(kshf.LOG.FILTER_TEXTSEARCH, {id:me.summaryFilter.id, info:v});
                        }
                    }
                }, 750);
            })
            ;
    },
    /** returns the maximum active aggregate value per row in chart data */
    getMaxAggr_Active: function(){
        return d3.max(this._cats, function(cat){ return cat.aggregate_Active; });
    },
    /** returns the maximum total aggregate value stored per row in chart data */
    getMaxAggr_Total: function(){
        if(this._cats===undefined) return 0;
        var subMax=0;
        // recurse
        if(this.subFacets.length>0){
            subMax = d3.max(this.subFacets, function(f){ return f.getMaxAggr_Total(v); });
        }
        if(!this.hasCategories()) return subMax;
        if(this._maxBarValueMaxPerAttrib) return this._maxBarValueMaxPerAttrib;
        this._maxBarValueMaxPerAttrib = d3.max(this._cats, function(d){ return d.aggregate_Total;});
        return this._maxBarValueMaxPerAttrib;
    },
    /** -- */
    _update_Selected: function(){
        if(this.DOM.root) {
            this.DOM.root
                .attr("filtered",this.isFiltered())
                .attr("filtered_or",this.summaryFilter.selected_OR.length)
                .attr("filtered_and",this.summaryFilter.selected_AND.length)
                .attr("filtered_not",this.summaryFilter.selected_NOT.length)
                .attr("filtered_total",this.summaryFilter.selectedCount_Total())
                ;
        }
        var show_box = (this.summaryFilter.selected_OR.length+this.summaryFilter.selected_AND.length)>1;
        this.summaryFilter.selected_OR.forEach(function(attrib){
            attrib.DOM.facet.setAttribute("show-box",show_box);
        },this);
        this.summaryFilter.selected_AND.forEach(function(attrib){
            attrib.DOM.facet.setAttribute("show-box",show_box);
        },this);
        this.summaryFilter.selected_NOT.forEach(function(attrib){
            attrib.DOM.facet.setAttribute("show-box","true");
        },this);
    },
    /** -- */
    unselectAllAttribs: function(){
        this._cats.forEach(function(cat){
            if(cat.f_selected() && cat.DOM.facet) cat.DOM.facet.setAttribute("highlight",false);
            cat.set_NONE();
        });
        this.summaryFilter.selected_All_clear();
    },
    /** -- */
    selectAllAttribsButton: function(){
        this._cats.forEach(function(attrib){
            if(!attrib.selectedForLink) return;
            attrib.set_OR(this.summaryFilter.selected_OR);
        },this);
        this._update_Selected();
        this.summaryFilter.how="All";
        this.summaryFilter.addFilter(true);
        if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_ADD_OR_ALL, {id: this.summaryFilter.id} );
    },
    /** -- */
    setCollapsed: function(v){
        kshf.Summary_Base.prototype.setCollapsed.call(this,v);
        // collapse children only if this is a hierarchy, not sub-filtering
        if(this.hasSubFacets() && !this.hasCategories()){
            this.subFacets.forEach(function(f){ f.setCollapsed(v); });
        }
        return this; // allow chaining
    },
    /** -- */
    clearCatTextSearch: function(){
        if(!this.showTextSearch) return;
        this.DOM.attribTextSearchControl.attr("showClear",false);
        this.DOM.attribTextSearchInput[0][0].value = '';
    },
    /** -- */
    scrollBarShown: function(){
        return this.attribHeight<this.catCount_Total*this.heightRow_category;
    },
    /** -- */
    getWidth_CatChart: function(){
        // This will make the bar width extend over to the scroll area.
        // Doesn't look better, the amount of space saved makes chart harder to read and breaks the regularly spaced flow.
        /*if(!this.scrollBarShown()){
            return this.panel.width_catBars+kshf.scrollWidth-5;
        }*/
        return this.panel.width_catBars;
    },
    /** -- */
    updateBarPreviewScale2Active: function(){
        if(!this.hasCategories()) return; // nothing to do
        var me=this;

        this.chartScale_Measure
            .rangeRound([0, this.getWidth_CatChart()])
            .nice(this.chartAxis_Measure_TickSkip())
            .domain([
                0,
                (this.catBarScale==="scale_frequency")?
                    this.browser.itemsWantedCount:
                    this.getMaxAggr_Active()
            ])
            ;

        this.refreshViz_Active();
        this.refreshViz_Total();
        this.refreshViz_Compare();
        this.refreshViz_Axis();

        this.DOM.aggr_Preview.attr("fast",null); // take it slow for result preview animations
        this.refreshViz_Preview();
        setTimeout(function(){ me.DOM.aggr_Preview.attr("fast",true); },800);
    },
    /** -- */
    setHeight: function(newHeight){
        if(!this.hasCategories()) return;
        var attribHeight_old = this.attribHeight;
        var attribHeight_new = Math.min(
            newHeight-this.getHeight_Header()-this.getHeight_Config()-this.getHeight_Bottom()+2,
            this.heightRow_category*this.catCount_Visible);

//        if(this.attribHeight===attribHeight_new) return;
        this.attribHeight = attribHeight_new;

        // update catCount_InDisplay
        var c = Math.floor(this.attribHeight / this.heightRow_category);
        var c = Math.floor(this.attribHeight / this.heightRow_category);
        if(c<0) c=1;
        if(c>this.catCount_Visible) c=this.catCount_Visible;
        if(this.catCount_Visible<=2){
            c = this.catCount_Visible;
        } else {
            c = Math.max(c,2);
        }
        this.catCount_InDisplay = c+1;
        this.catCount_InDisplay = Math.min(this.catCount_InDisplay,this.catCount_Visible);

        this.refreshScrollDisplayMore(this.cat_InDisplay_First+this.catCount_InDisplay);

        this.updateAttribCull();
        this.cullAttribs();

        this.DOM.headerGroup.select(".buttonSummaryExpand").style("display",
            (this.panel.getNumOfOpenSummaries()<=1||this.areAllCatsInDisplay())?
                "none":
                "inline-block"
        );

        this.updateBarPreviewScale2Active();

        if(this.cbSetHeight && attribHeight_old!==attribHeight_new) this.cbSetHeight(this);
    },
    /** -- */
    updateAfterFilter: function(resultChange){
        if(!this.hasCategories()) return;
        this.refreshMeasureLabel();
        this.updateBarPreviewScale2Active();

        if(this.show_cliques) {
            this.dirtySort = true;
            this.DOM.root.attr("refreshSorting",true);
        }

        if(!this.dirtySort) {
            this.updateCatSorting();
        } else {
            this.refreshViz_All();
            this.refreshViz_Active();
        }
    },
    /** -- */
    refreshWidth: function(){
        if(this.DOM.facetCategorical){
            this.DOM.facetCategorical.style("width",this.getWidth()+"px");
            this.DOM.summaryTitle.style("max-width",(this.getWidth()-40)+"px");
            this.DOM.chartAxis_Measure.select(".chartAxis_Measure_background")
                .style("width",(this.getWidth()-this.panel.width_catMeasureLabel-this.getWidth_Label())+"px");
            this.refreshViz_Axis();
        }
    },
    /** -- */
    refreshMeasureLabel: function(){
        if(!this.hasCategories()) return;
        if(this.browser.previewedSelectionSummary===this && !this.hasMultiValueItem) return;

        var me=this;

        this.DOM.cats.attr("noitems",function(aggr){ return !me.isAttribSelectable(aggr); });

        this.DOM.measureLabel.each(function(attrib){
            if(attrib.isCulled) return;
            var p=attrib.aggregate_Preview;
            if(me.browser.vizPreviewActive){
                if(me.browser.preview_not)
                    p = attrib.aggregate_Active-attrib.aggregate_Preview;
                else
                    p = attrib.aggregate_Preview;
            } else {
                p = attrib.aggregate_Active;
            }
            if(me.browser.percentModeActive){
                if(attrib.aggregate_Active===0){
                    this.textContent = "";
                } else {
                    if(me.browser.ratioModeActive){
                        if(!me.browser.vizPreviewActive){
                            this.textContent = "";
                            return;
                        }
                        p = 100*p/attrib.aggregate_Active;
                    } else {
                        p = 100*p/me.browser.itemsWanted_Aggregrate_Total;
                    }
                    if(p<0) p=0;
                    this.textContent = p.toFixed(0)+"%";
                }
            } else {
                if(p<0) p=0;
                this.textContent = kshf.Util.formatForItemCount(p);
            }
        });
    },
    /** -- */
    refreshViz_All: function(){
        if(!this.hasCategories() || this.collapsed) return;
        var me=this;
        this.refreshViz_Total();
        this.refreshViz_Active();

        this.DOM.aggr_Preview.attr("fast",null); // take it slow for result preview animations
        this.refreshViz_Preview();
        setTimeout(function(){ me.DOM.aggr_Preview.attr("fast",true); },800);

        this.refreshViz_Compare();
        this.refreshMeasureLabel();
        this.refreshViz_Axis();
    },
    /** -- */
    refreshViz_Total: function(){
        if(!this.hasCategories() || this.collapsed) return;
        var me = this;
        // Do not need to update total. Total value is invisible. Percent view is based on active count.
        if(!this.browser.ratioModeActive){
            this.DOM.aggr_Total.each(function(attrib){
                kshf.Util.setTransform(this,
                    "scaleX("+me.chartScale_Measure(attrib.aggregate_Total)+")");
            });
            this.DOM.aggr_TotalTip.each(function(attrib){
                kshf.Util.setTransform(this,
                    "translateX("+me.chartScale_Measure(attrib.aggregate_Total)+"px)");
            }).style("opacity",function(attrib){
                return (attrib.aggregate_Total>me.chartScale_Measure.domain()[1])?1:0;
            });
        } else {
            this.DOM.aggr_TotalTip.style("opacity",0);
        }
    },
    /** -- */
    refreshViz_Active: function(){
        if(!this.hasCategories() || this.collapsed) return;
        var me=this, ratioMode=this.browser.ratioModeActive, maxWidth = this.chartScale_Measure.range()[1];
        var width_Text = this.getWidth_Label()+this.panel.width_catMeasureLabel;
        this.DOM.aggr_Active.each(function(category){
            kshf.Util.setTransform(this,"scaleX("+(ratioMode?
                ((category.aggregate_Active===0)?0:maxWidth):
                me.chartScale_Measure(category.aggregate_Active)
            )+")");
        });
        var func_clickAreaScale=function(category){
            return width_Text+(ratioMode?
                ((category.aggregate_Active===0)?0:maxWidth):
                me.chartScale_Measure(category.aggregate_Active)
            )+"px";
        };
        this.DOM.attribClickArea.style("width",func_clickAreaScale);
        this.DOM.compareButton
            .style("left",func_clickAreaScale)
            .attr("inside",function(category){
                if(ratioMode) return "";
                if(maxWidth-me.chartScale_Measure(category.aggregate_Active)<10) return "";
            });
    },
    /** -- */
    refreshViz_Preview: function(){
        if(!this.hasCategories() || this.collapsed) return;
        var me=this, ratioMode=this.browser.ratioModeActive, maxWidth = this.chartScale_Measure.range()[1];
        this.DOM.aggr_Preview.each(function(aggr){
            var p=aggr.aggregate_Preview;
            if(me.browser.preview_not) p = aggr.aggregate_Active-p;
            kshf.Util.setTransform(this,"scaleX("+(
                ratioMode ? ((p/aggr.aggregate_Active)*maxWidth ) : me.chartScale_Measure(p)
            )+")");
        });
        this.refreshMeasureLabel();
    },
    /** Gets the active previewed value, and stores it in the cache */
    cachePreviewValue: function(){
        if(!this.hasCategories() || this.collapsed) return;
        var preview_not=this.browser.preview_not;
        this.DOM.aggr_Preview.each(function(aggr){
            aggr.aggregate_Compare = aggr.aggregate_Preview;
            if(preview_not) {
                aggr.aggregate_Compare = aggr.aggregate_Active-aggr.aggregate_Compare;
            }
        });
    },
    /** -- */
    refreshViz_Compare: function(){
        if(!this.hasCategories() || this.collapsed) return;
        if(!this.browser.vizCompareActive) return;
        var me=this, ratioMode=this.browser.ratioModeActive, maxWidth = this.chartScale_Measure.range()[1];
        if(this.browser.vizCompareActive){
            this.DOM.aggr_Compare.each(function(cat){
                kshf.Util.setTransform(this,"scaleX("+(
                    ratioMode ? ((cat.aggregate_Compare/cat.aggregate_Active)*maxWidth) : me.chartScale_Measure(cat.aggregate_Compare)
                )+")");
            });
        }
    },
    /** -- */
    clearViz_Preview: function(){
        if(!this.hasCategories()) return;
        this._cats.forEach(function(cat){
            cat.updatePreview_Cache = false;
        });
        if(this.collapsed) return;
        this.DOM.aggr_Preview.each(function(cat){
            cat.aggregate_Preview=0;
            if(cat.aggregate_Compare===0) return;
            kshf.Util.setTransform(this,"scaleX(0)");
        });
        this.refreshMeasureLabel();
    },
    /** -- */
    refreshViz_Axis: function(){
        if(!this.hasCategories()) return;
        var me=this;

        var tickValues;
        var transformFunc;

        var maxValue;

        var chartWidth = this.getWidth_CatChart();

        if(this.browser.ratioModeActive) {
            maxValue = 100;
            tickValues = d3.scale.linear()
                .rangeRound([0, chartWidth])
                .nice(this.chartAxis_Measure_TickSkip())
                .clamp(true)
                .domain([0,100])
                .ticks(this.chartAxis_Measure_TickSkip());
        } else {
            if(this.browser.percentModeActive) {
                maxValue = Math.round(100*me.getMaxAggr_Active()/me.browser.itemsWantedCount);
                tickValues = d3.scale.linear()
                    .rangeRound([0, chartWidth])
                    .nice(this.chartAxis_Measure_TickSkip())
                    .clamp(true)
                    .domain([0,maxValue])
                    .ticks(this.chartAxis_Measure_TickSkip());
            } else {
                tickValues = this.chartScale_Measure.ticks(this.chartAxis_Measure_TickSkip())
            }
        }

        // remove non-integer values & 0...
        tickValues = tickValues.filter(function(d){return d%1===0&&d!==0;});

        var tickDoms = this.DOM.chartAxis_Measure.selectAll("span.tick").data(tickValues,function(i){return i;});

        if(this.browser.ratioModeActive){
            transformFunc=function(d){
                kshf.Util.setTransform(this,"translateX("+(d*chartWidth/100-0.5)+"px)");
            };
        } else {
            if(this.browser.percentModeActive) {
                transformFunc=function(d){
                    kshf.Util.setTransform(this,"translateX("+((d/maxValue)*chartWidth-0.5)+"px)");
                };
            } else {
                transformFunc=function(d){
                    kshf.Util.setTransform(this,"translateX("+(me.chartScale_Measure(d)-0.5)+"px)");
                };
            }
        }

        var x=this.browser.noAnim;

        if(x===false) this.browser.setNoAnim(true);
        var tickData_new=tickDoms.enter().append("span").attr("class","tick").each(transformFunc);
        if(x===false) this.browser.setNoAnim(false);

        // translate the ticks horizontally on scale
        tickData_new.append("span").attr("class","line")
            .style("top","-"+(this.attribHeight+3)+"px")
            .style("height",(this.attribHeight-1)+"px");

        if(this.browser.ratioModeActive){
            tickData_new.append("span").attr("class","text").text(function(d){return d;});
        } else {
            tickData_new.append("span").attr("class","text").text(function(d){return d3.format("s")(d);});
        }
        if(this.configRowCount>0){
            var h=this.attribHeight;
            var hm=tickData_new.append("span").attr("class","text text_upper").style("top",(-h-19)+"px");
            if(this.browser.ratioModeActive){
                hm.text(function(d){return d;});
            } else {
                hm.text(function(d){return d3.format("s")(d);});
            }
        }

        setTimeout(function(){
            me.DOM.chartAxis_Measure.selectAll("span.tick").style("opacity",1).each(transformFunc);
        });

        tickDoms.exit().remove();
    },
    /** -- */
    refreshLabelWidth: function(){
        if(!this.hasCategories()) return;
        if(this.DOM.facetCategorical===undefined) return;
        var labelWidth = this.getWidth_Label();
        var barChartMinX = labelWidth + this.panel.width_catMeasureLabel;

        this.DOM.chartCatLabelResize.style("left",(labelWidth+1)+"px");
        this.DOM.facetCategorical.selectAll(".hasLabelWidth").style("width",labelWidth+"px");
        this.DOM.item_count_wrapper
            .style("left",labelWidth+"px")
            .style("width",this.panel.width_catMeasureLabel+"px")
            ;
        this.DOM.chartAxis_Measure.each(function(d){
            kshf.Util.setTransform(this,"translateX("+barChartMinX+"px)");
        });
        this.DOM.catSortButton.style("left",labelWidth+"px");
        this.DOM.aggr_Group.style("left",barChartMinX+"px");
        if(this.DOM.catSortButton)
            this.DOM.catSortButton.style("width",this.panel.width_catMeasureLabel+"px");
    },
    /** -- */
    refreshScrollDisplayMore: function(bottomItem){
        if(this.catCount_Total<=4) {
            this.DOM.scroll_display_more.style("display","none");
            return;
        }
        var moreTxt = ""+this.catCount_Visible+" "+kshf.lang.cur.Rows;
        var below = this.catCount_Visible-bottomItem;
        if(below>0) moreTxt+=", <span class='fa fa-angle-down'></span> "+below+" "+kshf.lang.cur.More;
        this.DOM.scroll_display_more.html(moreTxt);
    },
    /** -- */
    refreshHeight: function(){
        // Note: if this has attributes, the total height is computed from height of the children by html layout engine.
        // So far, should be pretty nice.
        if(!this.hasCategories()) return;

        this.DOM.wrapper.style("height",(this.collapsed?"0":this.getHeight_Content())+"px");
        this.DOM.attribGroup.style("height",this.attribHeight+"px"); // 1 is for borders...
        this.DOM.root.style("max-height",(this.getHeight()+1)+"px");

        var h=this.attribHeight;
        this.DOM.chartAxis_Measure.selectAll(".line").style("top",(-h+1)+"px").style("height",(h-2)+"px");
        this.DOM.chartAxis_Measure.selectAll(".text_upper").style("top",(-h-19)+"px");
    },
    /** -- */
    setHeightRow_attrib: function(h){
        var me=this;
        if(this.heightRow_category===h) return;
        this.heightRow_category = h;

        this.browser.setNoAnim(true);

        this.browser.updateLayout();

        this.DOM.cats.each(function(attrib){
            kshf.Util.setTransform(this,
                "translate("+attrib.posX+"px,"+(me.heightRow_category*attrib.orderIndex)+"px)");
            this.style.marginTop = ((me.heightRow_category-18)/2)+"px";
        });
        this.DOM.chartBackground.style("height",this.getTotalAttribHeight()+"px");
        this.DOM.chartCatLabelResize.style("height",this.getTotalAttribHeight()+"px");

        setTimeout(function(){ me.browser.setNoAnim(false); },100);
    },
    /** -- */
    isAttribVisible: function(attrib){
        if(this.isLinked){
            if(attrib.selectedForLink===false) return false;
            return true;
        }

        // Show selected attribute always
        if(attrib.f_selected()) return true;
        // Show if number of active items is not zero
        if(attrib.aggregate_Active!==0) return true;
        // Show if item has been "isWanted" by some active sub-filtering
        if(this.catCount_Wanted < this.catCount_Total && attrib.isWanted) return true;
        // if inactive attributes are not removed, well, don't remove them...
        if(this.removeInactiveCats===false) return true;
        // summary is not filtered yet, cannot click on 0 items
        if(!this.isFiltered()) return attrib.aggregate_Active!==0;
        // Hide if multiple options are selected and selection is and
//        if(this.summaryFilter.selecttype==="SelectAnd") return false;
        // TODO: Figuring out non-selected, zero-active-item attribs under "SelectOr" is tricky!

//        if(attrib.orderIndex===this.catCount_Total) return true;

        if(attrib.isWanted===false) return false;
        return true;
    },
    /** -- */
    isAttribSelectable: function(attrib){
        // Show selected attribute always
        if(attrib.f_selected()) return true;
        // Show if number of active items is not zero
        if(attrib.aggregate_Active!==0) return true;
        // Show if multiple attributes are selected and the summary does not include multi value items
        if(this.isFiltered() && !this.hasMultiValueItem) return true;
        // Hide
        return false;
    },
    /** When clicked on an attribute ... */
    /* what: AND / OR / NOT */
    filterAttrib: function(attrib, what, how){
        if(this.browser.skipSortingFacet){
            // you can now sort the last filtered summary, attention is no longer there.
            this.browser.skipSortingFacet.dirtySort = false;
            this.browser.skipSortingFacet.DOM.root.attr("refreshSorting",false);
        }
        this.browser.skipSortingFacet=this;
        this.browser.skipSortingFacet.dirtySort = true;
        this.browser.skipSortingFacet.DOM.root.attr("refreshSorting",true);

        var i=0;

        var preTest = (this.summaryFilter.selected_OR.length>0 && (this.summaryFilter.selected_AND.length>0 ||
                this.summaryFilter.selected_NOT.length>0));

        // if selection is in same mode, "undo" to NONE.
        if(what==="NOT" && attrib.is_NOT()) what = "NONE";
        if(what==="AND" && attrib.is_AND()) what = "NONE";
        if(what==="OR"  && attrib.is_OR() ) what = "NONE";

        if(what==="NONE"){
            if(attrib.is_AND() || attrib.is_NOT()){
                this.summaryFilter.how = "MoreResults";
            }
            if(attrib.is_OR()){
                this.summaryFilter.how = this.summaryFilter.selected_OR.length===0?"MoreResults":"LessResults";
            }
            attrib.set_NONE();
            if(this.summaryFilter.selected_OR.length===1 && this.summaryFilter.selected_AND.length===0){
                this.summaryFilter.selected_OR.forEach(function(a){
                    a.set_NONE();
                    a.set_AND(this.summaryFilter.selected_AND);
                },this);
            }
            if(!this.summaryFilter.selected_Any()){
                this.dirtySort = false;
                this.DOM.root.attr("refreshSorting",false);
            }
            if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_UNSELECT, {id:this.summaryFilter.id, info:attrib.id()});
        }
        if(what==="NOT"){
            if(attrib.is_NONE()){
                if(attrib.aggregate_Active===this.browser.itemsWantedCount){
                    alert("Removing this category will create an empty result list, so it is not allowed.");
                    return;
                }
                this.summaryFilter.how = "LessResults";
            } else {
                this.summaryFilter.how = "All";
            }
            attrib.set_NOT(this.summaryFilter.selected_NOT);
            if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_ADD_NOT, {id:this.summaryFilter.id, info:attrib.id()});
        }
        if(what==="AND"){
            attrib.set_AND(this.summaryFilter.selected_AND);
            this.summaryFilter.how = "LessResults";
            if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_ADD_AND, {id:this.summaryFilter.id, info:attrib.id()});
        }
        if(what==="OR"){
            if(!this.hasMultiValueItem && this.summaryFilter.selected_NOT.length>0){
                var temp = [];
                this.summaryFilter.selected_NOT.forEach(function(a){ temp.push(a); });
                temp.forEach(function(a){ a.set_NONE(); });
            }
            if(this.summaryFilter.selected_OR.length===0 && this.summaryFilter.selected_AND.length===1){
                this.summaryFilter.selected_AND.forEach(function(a){
                    a.set_NONE();
                    a.set_OR(this.summaryFilter.selected_OR);
                },this);
            }
            attrib.set_OR(this.summaryFilter.selected_OR);
            this.summaryFilter.how = "MoreResults";
            if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_ADD_OR, {id:this.summaryFilter.id, info:attrib.id()});
        }
        if(how) this.summaryFilter.how = how;

        if(preTest){
            this.summaryFilter.how = "All";
        }
        if(this.summaryFilter.selected_OR.length>0 && (this.summaryFilter.selected_AND.length>0 ||
                this.summaryFilter.selected_NOT.length>0)){
            this.summaryFilter.how = "All";
        }

        if(this.summaryFilter.selectedCount_Total()===0){
            this.summaryFilter.clearFilter();
            return;
        }
        this.clearCatTextSearch();
        this.summaryFilter.linkFilterSummary = "";
        this.summaryFilter.addFilter(true);
    },
    /** -- */
    cbAttribEnter: function(attrib){
        this.browser.previewedSelectionSummary = this;

        var me=this;

        if(attrib.cliqueRow)
            attrib.cliqueRow.setAttribute("highlight","selected");

        if(this.isAttribSelectable(attrib)) {
            attrib.DOM.facet.setAttribute("selecttype","and");
            attrib.DOM.facet.setAttribute("highlight","selected");
            if(!this.hasMultiValueItem && this.summaryFilter.selected_AND.length!==0) {
                return;
            }
            attrib.highlightAll(true);
            var timeoutTime = kshf.previewTimeoutMS;
            if(this.browser.vizCompareActive) timeoutTime = 0;
//            this.resultPreviewShowTimeout = setTimeout(function(){
                if(!me.browser.pauseResultPreview &&
                  (me.hasMultiValueItem || me.summaryFilter.selected_AND.length===0) &&
                  (!attrib.is_NOT()) ){
                    // calculate the preview
                    attrib.items.forEach(function(item){item.updatePreview(me.parentFacet);},me);
                    me.browser.itemCount_Previewed = attrib.aggregate_Preview;
                    attrib.DOM.facet.setAttribute("showlock",true);
                    me.browser.refreshResultPreviews(attrib);
                    if(sendLog) {
                        if(me.resultPreviewLogTimeout) clearTimeout(me.resultPreviewLogTimeout);
                        me.resultPreviewLogTimeout = setTimeout(function(){
                            sendLog(kshf.LOG.FILTER_PREVIEW, {id:me.summaryFilter.id, info: attrib.id()});
                        }, 1000); // wait 1 second to see the update fully
                    }
                }
//            },timeoutTime);
        } else {
            if(this.tipsy_title===undefined) return;
        }
    },
    /** -- */
    cbAttribLeave: function(attrib){
        this.browser.previewedSelectionSummary = null;

        if(attrib.skipMouseOut !==undefined && attrib.skipMouseOut===true){
            attrib.skipMouseOut = false;
            return;
        }

        if(attrib.cliqueRow)
            attrib.cliqueRow.setAttribute("highlight",false);

        if(!this.isAttribSelectable(attrib)) return;
        attrib.nohighlightAll(true);

        if(this.resultPreviewLogTimeout){
            clearTimeout(this.resultPreviewLogTimeout);
        }
        this.browser.items.forEach(function(item){
            if(item.DOM.record) item.DOM.record.setAttribute("highlight",false);
        },this);

        if(!this.browser.pauseResultPreview){
            attrib.DOM.facet.setAttribute("showlock",false);
            this.browser.clearResultPreviews();
        }

        if(this.resultPreviewShowTimeout){
            clearTimeout(this.resultPreviewShowTimeout);
            this.resultPreviewShowTimeout = null;
        }
    },
    /** - */
    insertCategories: function(){
        var me = this;
        this.resultPreviewLogTimeout = null;

        var DOM_cats_new = this.DOM.attribGroup.selectAll(".attrib")
            .data(this._cats, function(category){ return category.id(); })
        .enter().append("span").attr("class","attrib")
            .attr("highlight",false)
            .attr("showlock" ,false)
            .attr("selected",0)
            .each(function(category){
                category.facet = me;
                category.DOM.facet = this;
                category.isVisible = true;
                this.isLinked = me.isLinked;

                category.pos_y = 0;
                kshf.Util.setTransform(this,"translateY(0px)");
            })
            .on("mouseover",function(category){ me.cbAttribEnter(category);})
            .on("mouseleave",function(category){ me.cbAttribLeave(category);})
            .attr("title",me.catTooltip?function(cat){ return me.catTooltip.call(cat.data); }:null);
            ;
        this.updateAttribCull();

        var cbAttribClick = function(attrib){
            if(!me.isAttribSelectable(attrib)) return;

            if(this.timer){ // double click
                if(!me.hasMultiValueItem) return;
                me.unselectAllAttribs();
                me.filterAttrib("AND","All");
                if(sendLog) sendLog(kshf.LOG.FILTER_ATTR_EXACT,{id: me.summaryFilter.id, info: attrib.id()});
                return;
            } else {
                if(attrib.is_NOT()){
                    me.filterAttrib(attrib,"NOT");
                } else if(attrib.is_AND()){
                    me.filterAttrib(attrib,"AND");
                } else if(attrib.is_OR()){
                    me.filterAttrib(attrib,"OR");
                } else {
                    // remove the single selection if it is defined with OR
                    if(!me.hasMultiValueItem && me.summaryFilter.selected_Any()){
                        if(me.summaryFilter.selected_OR.indexOf(attrib)<0){
                            var temp = [];
                            me.summaryFilter.selected_OR.forEach(function(a){ temp.push(a); });
                            temp.forEach(function(a){ a.set_NONE(); });
                        }
                        if(me.summaryFilter.selected_AND.indexOf(attrib)<0){
                            var temp = [];
                            me.summaryFilter.selected_AND.forEach(function(a){ temp.push(a); });
                            temp.forEach(function(a){ a.set_NONE(); });
                        }
                        if(me.summaryFilter.selected_NOT.indexOf(attrib)<0){
                            var temp = [];
                            me.summaryFilter.selected_NOT.forEach(function(a){ temp.push(a); });
                            temp.forEach(function(a){ a.set_NONE(); });
                        }
                        me.filterAttrib(attrib,"AND","All");
                    } else {
                        me.filterAttrib(attrib,"AND");
                    }
                }
            }
            if(me.hasMultiValueItem){
                var x = this;
                this.timer = setTimeout(function() { x.timer = null; }, 500);
            }
        };

        var dragged;
        var draggedAttrib = null;
        var attribDrag = function(d){
            this.addEventListener("dragstart", function( event ) {
                // store a ref. on the dragged elem
                dragged = event.target;
                draggedAttrib = d;
                // make it half transparent
                event.target.style.opacity = .5;
            }, false);
            this.addEventListener("dragend", function( event ) {
                // reset the transparency
                event.target.style.opacity = "";
                draggedAttrib = null;
            }, false);
            this.addEventListener("dragover", function( event ) {
                // prevent default to allow drop
                event.preventDefault();
            }, false);
            this.addEventListener("dragenter", function( event ) {
                // highlight potential drop target when the draggable element enters it
                if(draggedAttrib) {
                    event.target.style.background = "rgba(0,0,150,0.5)";
                }
            }, false);
            this.addEventListener("dragleave", function( event ) {
                // reset background of potential drop target when the draggable element leaves it
                if(draggedAttrib) {
                    event.target.style.background = "";
                }
            }, false);
            this.addEventListener("drop", function( event ) {
                // prevent default action (open as link for some elements)
                event.preventDefault();
                // move dragged elem to the selected drop target
                if ( event.target.className == "clickArea" ) {
                    event.target.style.background = "";
                    var item1 = dragged.__data__;
                    var item2 = event.target.__data__;
                    me._cats[item2.orderIndex] = item1;
                    me._cats[item1.orderIndex] = item2;
                    var tmp = item2.orderIndex
                    item2.orderIndex = item1.orderIndex;
                    item1.orderIndex = tmp;

                    item1.DOM.facet.tipsy.hide();
                    item2.DOM.facet.tipsy.hide();
                    item2.DOM.facet.setAttribute("highlight",false);
                    item2.DOM.facet.setAttribute("highlight",false);

                    me.DOM.cats.each(function(attrib){
                        if(attrib.isVisible){
                            attrib.posX = 0;
                            attrib.posY = me.heightRow_category*attrib.orderIndex;
                            attrib.posY = me.heightRow_category*attrib.orderIndex;
                            kshf.Util.setTransform(this,"translate("+attrib.posX+"px,"+attrib.posY+"px)");
                        }
                    });

                    if(me.cbFacetSort) me.cbFacetSort.call(me);
                }
            }, false);
        };

        var cbOrEnter = function(attrib){
            me.browser.clearResultPreviews();
            attrib.DOM.facet.setAttribute("selecttype","or");
            if(me.summaryFilter.selected_OR.length>0)
                me.browser.clearResultPreviews();
            d3.event.stopPropagation();
        };
        var cbOrLeave = function(attrib){
            attrib.DOM.facet.setAttribute("selecttype","and");
        };
        var cbOrClick = function(attrib){
            me.filterAttrib(attrib,"OR");
            d3.event.stopPropagation();
            d3.event.preventDefault();
        };

        var cbNotEnter = function(attrib){
            attrib.DOM.facet.setAttribute("selecttype","not");
            me.browser.preview_not = true;
            me.browser.refreshResultPreviews(attrib);
            d3.event.stopPropagation();
        };
        var cbNotLeave = function(attrib){
            attrib.DOM.facet.setAttribute("selecttype","and");
            me.browser.preview_not = false;
            me.browser.clearResultPreviews();
        };
        var cbNotClick = function(attrib){
            me.browser.preview_not = true;
            me.filterAttrib(attrib,"NOT");
            setTimeout(function(){ me.browser.preview_not = false; }, 1000);
            d3.event.stopPropagation();
            d3.event.preventDefault();
        };

        var domAttrLabel = DOM_cats_new.append("span").attr("class", "attribLabel hasLabelWidth");

        var filterButtons = domAttrLabel.append("span").attr("class", "filterButtons");
            filterButtons.append("span").attr("class","filterButton notButton")
                .text(kshf.lang.cur.Not)
                .on("mouseover",cbNotEnter)
                .on("mouseout",cbNotLeave)
                .on("click",cbNotClick);
            filterButtons.append("span").attr("class","filterButton orButton")
                .text(kshf.lang.cur.Or)
                .on("mouseover",cbOrEnter)
                .on("mouseout",cbOrLeave)
                .on("click",cbOrClick)
                ;

        this.DOM.theLabel = domAttrLabel.append("span").attr("class","theLabel").html(function(category){
            return me.catLabel.call(category.data);
        });

        DOM_cats_new.append("span").attr("class", "item_count_wrapper")
            .append("span").attr("class","measureLabel");

        var domBarGroup = DOM_cats_new.append("span").attr("class","aggr_Group");
        domBarGroup.append("span").attr("class", "aggr total");
        domBarGroup.append("span").attr("class", "aggr total_tip");
        domBarGroup.append("span").attr("class", "aggr active");
        domBarGroup.append("span").attr("class", "aggr preview").attr("fast",true);
        domBarGroup.append("span").attr("class", "aggr compare").attr("hidden",true);

        DOM_cats_new.append("span").attr("class", "clickArea")
            .attr("draggable",true)
            .on("click", cbAttribClick)
            .each(attribDrag)
            ;

        DOM_cats_new.append("span").attr("class","compareButton fa")
            .each(function(category){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w',
                    title: function(){
                        return (me.browser.comparedAggregate!==category)?
                            kshf.lang.cur.LockToCompare:kshf.lang.cur.Unlock;
                    }
                });
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("click",function(attrib){
                this.tipsy.hide();
                me.browser.setPreviewCompare(attrib);
                d3.event.stopPropagation();
            })
            ;

        this.DOM.cats = this.DOM.attribGroup.selectAll(".attrib")
        this.DOM.attribClickArea = this.DOM.cats.selectAll(".clickArea");
        this.DOM.compareButton = this.DOM.cats.selectAll(".compareButton");
        this.DOM.item_count_wrapper = this.DOM.cats.selectAll(".item_count_wrapper");
        this.DOM.measureLabel = this.DOM.cats.selectAll(".item_count_wrapper > .measureLabel");

        this.DOM.aggr_Group    = this.DOM.cats.selectAll(".aggr_Group");
        this.DOM.aggr_Total    = this.DOM.aggr_Group.selectAll(".total");
        this.DOM.aggr_TotalTip = this.DOM.aggr_Group.selectAll(".total_tip");
        this.DOM.aggr_Active   = this.DOM.aggr_Group.selectAll(".active");
        this.DOM.aggr_Preview  = this.DOM.aggr_Group.selectAll(".preview");
        this.DOM.aggr_Compare  = this.DOM.aggr_Group.selectAll(".compare");
    },
    /** -- */
    sortCategories: function(){
        var me = this;
        var inverse = this.catSortBy_Active.inverse;
        // Prepare sorting callback
        if(this.catSortBy_Active.prep) this.catSortBy_Active.prep.call(this);

        // idCompareFunc can be based on integer or string comparison
        var idCompareFunc = function(a,b){return b.id()-a.id();};
        if(typeof(this._cats[0].id())==="string")
            idCompareFunc = function(a,b){return b.id().localeCompare(a.id());};

        var theSortFunc;
        var sortV = this.catSortBy_Active.value;
        // sortV can only be function. Just having the check for sanity
        if(sortV && typeof sortV==="function"){
            // valueCompareFunc can be based on integer or string comparison
            var valueCompareFunc = function(a,b){return a-b;};
            if(typeof(sortV.call(this._cats[0].data, this._cats[0]))==="string")
                valueCompareFunc = function(a,b){return a.localeCompare(b);};

            // Of the value is a 2-parameter function, we'll expect that it defines a sorting order
            if(sortV.length===2){
                theSortFunc = sortV;
            } else {
                // The value is a custom value that returns an integer
                theSortFunc = function(a,b){
                    var x = valueCompareFunc(sortV.call(a.data,a),sortV.call(b.data,b));
                    if(x===0) x=idCompareFunc(a,b);
                    if(inverse) x=-x;
                    return x;
                };
            }
        } else {
            var sortFunc = function(a,b){
                var dif=b.aggregate_Active - a.aggregate_Active;
                if(dif===0) { return b.aggregate_Total-a.aggregate_Total; }
                return dif;
            };

            theSortFunc = function(a,b){
                // linked items...
                if(a.selectedForLink && !b.selectedForLink) return -1;
                if(b.selectedForLink && !a.selectedForLink) return 1;

                // selected on top of the list
                if(!a.f_selected() &&  b.f_selected()) return  1;
                if( a.f_selected() && !b.f_selected()) return -1;

                // put the items with zero active items to the end of list (may not be displayed)
                if(a.aggregate_Active===0 && b.aggregate_Active!==0) return  1;
                if(b.aggregate_Active===0 && a.aggregate_Active!==0) return -1;

                var x=sortFunc(a,b);
                if(x===0) x=idCompareFunc(a,b); // stable sorting. ID's would be string most probably.
                if(inverse) x=-x;
                return x;
            };
        }
        this._cats.sort(theSortFunc);
        this._cats.forEach(function(cat,i){ cat.orderIndex=i; });
    },
    /** -- */
    updateAttribCull: function(){
        var me=this;
        this._cats.forEach(function(attrib,i){
            attrib.isCulled_before = attrib.isCulled;
            // not visible if it is not within visible range...
            if(attrib.orderIndex<me.cat_InDisplay_First) {
                attrib.isCulled=true;
            }
            else if(attrib.orderIndex>me.cat_InDisplay_First+me.catCount_InDisplay) {
                attrib.isCulled=true;
            } else {
                attrib.isCulled=false;
            }
        });
    },
    /** -- */
    updateCatSorting: function(sortDelay,force,noAnim){
        if(this._cats===undefined) return;
        if(this._cats.length===0) return;
        if(this.uniqueCategories()) return; // Nothing to sort...
        if(this.catSortBy_Active.no_resort===true && force!==true) return;
        if(this.removeInactiveCats){
            this.updateCatCount_Visible();
        }

        var me = this;
        if(sortDelay===undefined) sortDelay = 1000;
        this.sortCategories();

        if(this.panel===undefined) return; // The rest deals with updating UI
        if(this.DOM.cats===undefined) return;

        this.updateAttribCull();

        var xRemoveOffset = -100;
        if(this.panel.name==='right') xRemoveOffset *= -1; // disappear to the other edge
        if(this.cbFacetSort) this.cbFacetSort.call(this);

        // filler is used to insert the scroll bar.
        // Items outside the view are not visible, something needs to expand the box
        this.DOM.chartBackground.style("height",this.getTotalAttribHeight()+"px");
        this.DOM.chartCatLabelResize.style("height",this.getTotalAttribHeight()+"px");

        var attribGroupScroll = me.DOM.attribGroup[0][0];
        // always scrolls to top row automatically when re-sorted
        if(this.scrollTop_cache!==0) kshf.Util.scrollToPos_do(attribGroupScroll,0);
        this.refreshScrollDisplayMore(this.cat_InDisplay_First+this.catCount_InDisplay);

        if(noAnim){
            this.DOM.cats.each(function(attrib){
                var x = 0;
                var y = me.heightRow_category*attrib.orderIndex;
                attrib.posX = x;
                attrib.posY = y;
                kshf.Util.setTransform(this,"translate("+x+"px,"+y+"px)");
            });
            return;
        }

        setTimeout(function(){
            // 1. Make items disappear
            // Note: do not cull with number of items made visible.
            // We are applying visible and block to ALL attributes as we animate the change
            me.DOM.cats.each(function(ctgry){
                if(ctgry.isVisible_before && !ctgry.isVisible){
                    // disappear into left panel...
                    this.style.opacity = 0;
                    ctgry.posX = xRemoveOffset;
                    ctgry.posY = ctgry.posY;
                    kshf.Util.setTransform(this,"translate("+ctgry.posX+"px,"+ctgry.posY+"px)");
                }
                if(!ctgry.isVisible_before && ctgry.isVisible){
                    // will be made visible...
                    ctgry.posY = me.heightRow_category*ctgry.orderIndex;
                    kshf.Util.setTransform(this,"translate("+xRemoveOffset+"px,"+ctgry.posY+"px)");
                }
                if(ctgry.isVisible || ctgry.isVisible_before){
                    this.style.visibility = "visible";
                    this.style.display = "block";
                }
            });

            // 2. Re-sort
            setTimeout(function(){
                me.DOM.cats.each(function(ctgry){
                    if(ctgry.isVisible && ctgry.isVisible_before){
                        ctgry.posX = 0;
                        ctgry.posY = me.heightRow_category*ctgry.orderIndex;
                        kshf.Util.setTransform(this,"translate("+ctgry.posX+"px,"+ctgry.posY+"px)");
                    }
                });

                // 3. Make items appear
                setTimeout(function(){
                    me.DOM.cats.each(function(ctgry){
                        if(!ctgry.isVisible_before && ctgry.isVisible){
                            this.style.opacity = 1;
                            ctgry.posX = 0;
                            ctgry.posY = me.heightRow_category*ctgry.orderIndex;
                            kshf.Util.setTransform(this,
                                "translate("+ctgry.posX+"px,"+ctgry.posY+"px)");
                        }
                    });
                    // 4. Apply culling
                    setTimeout(function(){ me.cullAttribs();} , 700);
                },(me.catCount_NowVisible>0)?300:0);

            },(me.catCount_NowInvisible>0)?300:0);

        },sortDelay);
    },
    /** -- */
    getTotalAttribHeight: function(){
        return this.catCount_Visible*this.heightRow_category;
    },
    /** -- */
    cullAttribs: function(){
        this.DOM.cats
            .style("visibility",function(attrib){
                return (attrib.isCulled || !attrib.isVisible)?"hidden":"visible";
            }).style("display",function(attrib){
                return (attrib.isCulled || !attrib.isVisible)?"none":"block";
            });

        if(this.cbCatCulled) this.cbCatCulled.call(this);
    },
    /** -- */
    chartAxis_Measure_TickSkip: function(){
        var width = this.chartScale_Measure.range()[1];
        var ticksSkip = width/25;
        if(this.getMaxAggr_Active()>100000){
            ticksSkip = width/30;
        }
        if(this.browser.percentModeActive){
            ticksSkip /= 1.1;
        }
        return ticksSkip;
    }
};

for(var index in Summary_Categorical_functions){
    kshf.Summary_Categorical.prototype[index] = Summary_Categorical_functions[index];
}



/**
 * KESHIF FACET - Categorical
 * @constructor
 */
kshf.Summary_Interval = function(){};
kshf.Summary_Interval.prototype = new kshf.Summary_Base();
var Summary_Interval_functions = {
    initialize: function(browser,name,attribFunc){
        kshf.Summary_Base.prototype.initialize.call(this,browser,name,attribFunc);
        this.type='interval';

        // Call the parent's constructor
        var me = this;

        // pixel width settings...
        this.height_hist = 1; // Initial width (will be updated later...)
        this.height_hist_min = 20; // Minimum possible histogram height
        this.height_hist_max = 100; // Maximim possible histogram height
        this.height_slider = 12; // Slider height
        this.height_labels = 13; // Height for labels
        this.height_percentile = 16; // Height for percentile chart
        this.height_hist_topGap = 12; // Height for histogram gap on top.

        this.width_barGap = 2; // The width between neighboring histgoram bars
        this.width_histMargin = 17; // ..
        this.width_vertAxisLabel = 23; // ..

        this.optimumTickWidth = 50;

        this.scaleType = 'linear'; // 'time', 'step', 'log'
        this.hasFloat = false;
        this.hasTime  = false;

        this.unitName = undefined; // the text appended to the numeric value (TODO: should not apply to time)
        this.showPercentile = false; // Percentile chart is a 1-line chart which shows %10-%20-%30-%40-%50 percentiles
        this.zoomed = false;

        this.histBins = [];
        this.intervalTicks = [];
        this.intervalRange = {};
        this.intervalTickFormat = function(v){
            if(!me.hasFloat) return d3.format("s")(v);
            return d3.format(".2f")(v);
        };

        if(this.items.length<=1000) this.initializeAggregates();
    },
    /** -- */
    initializeAggregates: function(){
        if(this.aggr_initialized) return;
        var me=this;
        var filterId = this.summaryFilter.id;
        this.itemV = function(item){ return item.mappedDataCache[filterId].v; };

        this.items.forEach(function(item){
            var v=this.summaryFunc.call(item.data,item);
            if(isNaN(v)) v=null;
            if(v===undefined) v=null;
            if(v!==null){
                if(v instanceof Date){
                    this.hasTime = true;
                } else {
                    if(typeof v!=='number'){
                        v = null;
                    } else{
                        this.hasFloat = this.hasFloat || v%1!==0;
                    }
                }
            }
            item.mappedDataCache[filterId] = {
                v: v,
                h: this,
            };
        },this);
        if(this.hasTime) this.setScaleType('time');

        // remove items that map to null / undefined
        this.filteredItems = this.items.filter(function(item){
            var v = me.itemV(item);
            return (v!==undefined && v!==null);
        });

        // Sort the items by their attribute value
        var sortValue = this.hasTime?
            function(a){ return me.itemV(a).getTime(); }:
            function(a){ return me.itemV(a); };
        this.filteredItems.sort(function(a,b){ return sortValue(a)-sortValue(b);});

        this.updateIntervalRangeMinMax();

        this.detectLogScale();

        // The default is for nugget viz...
        this.updateScaleAndBins(30,10);

        this.aggr_initialized = true;

        this.refreshViz_Nugget();
    },
    /** -- */
    detectLogScale: function(){
        if(this.scaleType==='time') return;
        var me = this;
        var filterId = this.summaryFilter.id;
        var activeItemV = function(item){
            // decide based on whether the items are in the visible range
            var v = item.mappedDataCache[filterId].v;
            if(v>=me.intervalRange.active.min && v <= me.intervalRange.active.max) return v;
        };
        var deviation = d3.deviation(this.filteredItems, activeItemV);
        var activeRange = this.intervalRange.active.max-this.intervalRange.active.min;
        if(deviation/activeRange<0.12 && this.intervalRange.active.min>=0){
            this.setScaleType('log');
        } else{
            if(this.scaleType==='log'){
                this.setScaleType("linear");
            }
        }
    },
    /** -- */
    createSummaryFilter: function(){
        var me=this;
        this.summaryFilter = this.browser.createFilter({
            parentSummary: this,
            onClear: function(summary){
                if(this.filteredBin){
                    this.filteredBin.setAttribute("filtered",false);
                    this.filteredBin = undefined;
                }
                summary.DOM.root.attr("filtered",false);
                if(summary.zoomed){
                    summary.setZoomed(false);
                }
                summary.resetIntervalFilterActive();
                summary.refreshIntervalSlider();
            },
            onFilter: function(summary){
                summary.DOM.root.attr("filtered",true);

                var i_min = this.active.min;
                var i_max = this.active.max;

                var isFilteredCb;
                if(summary.isFiltered_min() && summary.isFiltered_max()){
                    if(this.max_inclusive)
                        isFilteredCb = function(v){ return v>=i_min && v<=i_max; };
                    else
                        isFilteredCb = function(v){ return v>=i_min && v<i_max; };
                } else if(summary.isFiltered_min()){
                    isFilteredCb = function(v){ return v>=i_min; };
                } else {
                    if(this.max_inclusive)
                        isFilteredCb = function(v){ return v<=i_max; };
                    else
                        isFilteredCb = function(v){ return v<i_max; };
                }
                if(summary.scaleType==='step'){
                    if(i_min===i_max){
                        isFilteredCb = function(v){ return v===i_max; };
                    }
                }

                // TODO: Optimize: Check if the interval scale is extending/shrinking or completely updated...
                summary.items.forEach(function(item){
                    var v = item.mappedDataCache[this.id].v;
                    item.setFilterCache(this.id, (v!==null)?isFilteredCb(v):false);
                },this);

                if(summary.scaleType==="step"){
                    if(summary.zoomed) summary.DOM.zoomControl.attr("sign", "minus");
                } else {
                    summary.DOM.zoomControl.attr("sign", "plus");
                }

                summary.refreshIntervalSlider();
            },
            filterView_Detail: function(summary){
                var minValue = this.active.min;
                var maxValue = this.active.max;
                if(summary.scaleType==='step'){
                    if(minValue===maxValue) return "<b>"+minValue+"</b>";
                }
                if(summary.scaleType==='time'){
                    return "<b>"+summary.intervalTickFormat(minValue)+
                        "</b> to <b>"+summary.intervalTickFormat(maxValue)+"</b>";
                }
                if(summary.hasFloat){
                    minValue = minValue.toFixed(2);
                    maxValue = maxValue.toFixed(2);
                }
                if(summary.isFiltered_min() && summary.isFiltered_max()){
                    return "<b>"+minValue+"</b> to <b>"+maxValue+"</b>";
                } else if(summary.isFiltered_min()){
                    return "<b>at least "+minValue+"</b>";
                } else {
                    return "<b>at most "+maxValue+"</b>";
                }
            },
        });
    },
    /** -- */
    refreshViz_Nugget: function(){
        if(this.DOM.nugget===undefined) return;

        var nuggetChart = this.DOM.nugget.select(".nuggetChart");

        this.DOM.nugget
            .attr("aggr_initialized",this.aggr_initialized)
            .attr("datatype",this.getDataType());

        if(!this.aggr_initialized) return;

        if(this.uniqueCategories()){
            this.DOM.nugget.select(".nuggetInfo").html("<span class='fa fa-tag'></span><br>Unique");
            nuggetChart.style("display",'none');
            return;
        }

        var maxAggregate_Total = this.getMaxAggr_Total();

        if(this.intervalRange.min===this.intervalRange.max){
            this.DOM.nugget.select(".nuggetInfo").html("only<br>"+this.intervalRange.min);
            nuggetChart.style("display",'none');
            return;
        }

        var totalHeight = 17;
        nuggetChart.selectAll(".nuggetBar").data(this.histBins).enter()
                .append("span").attr("class","nuggetBar")
                .style("height",function(aggr){
                    return totalHeight*(aggr.length/maxAggregate_Total)+"px";
                })
            ;

        this.DOM.nugget.select(".nuggetInfo").html(
            "<span class='num_left'>"+this.intervalTickFormat(this.intervalRange.min)+"</span>"+
            "<span class='num_right'>"+this.intervalTickFormat(this.intervalRange.max)+"</span>");
    },
    /** -- */
    updateIntervalRangeMinMax: function(){
        this.intervalRange.min = d3.min(this.filteredItems,this.itemV);
        this.intervalRange.max = d3.max(this.filteredItems,this.itemV);
        this.intervalRange.active = {
            min: this.intervalRange.min,
            max: this.intervalRange.max
        };
        this.isEmpty = this.intervalRange.min===undefined;
        if(this.isEmpty) this.setCollapsed(true);
        this.resetIntervalFilterActive();
    },
    /** -- */
    resetIntervalFilterActive: function(){
        this.summaryFilter.active = {
            min: this.intervalRange.min,
            max: this.intervalRange.max
        };
    },
    /** -- */
    setScaleType: function(t){
        if(this.scaleType===t) return;
        var me=this;
        this.scaleType=t;

        if(this.DOM.facetInterval) this.DOM.facetInterval.attr("scaleType",this.scaleType);

        // remove items with value:0 (because log(0) is invalid)
        if(this.scaleType==='log' && (this.intervalRange.min===0 || this.intervalRange.max===0)) {
            this.filteredItems = this.filteredItems.filter(function(item){ return me.itemV(item)!==0; });
            this.updateIntervalRangeMinMax();
            if(this.panel===undefined){
                this.updateScaleAndBins(30,10);
            } else {
                var _width_ = this.getWidth()-this.width_histMargin-this.width_vertAxisLabel;
                this.updateScaleAndBins( _width_, Math.ceil(_width_/this.optimumTickWidth));
            }
        }
    },
    /** -- */
    getHeight: function(){
        if(this.collapsed) return this.getHeight_Header();
        // Note: I don't know why I need -2 to match real dom height.
        return this.getHeight_Header()+this.getHeight_Wrapper();
    },
    /** -- */
    getHeight_Wrapper: function(){
        return this.height_hist+this.getHeight_Extra();
    },
    /** -- */
    getHeight_Header: function(){
        return this.DOM.headerGroup[0][0].offsetHeight;
    },
    /** -- */
    getHeight_Extra: function(){
        return 7+this.height_hist_topGap+this.height_labels+this.height_slider+
            (this.showPercentile?this.height_percentile:0);
    },
    /** -- */
    getHeight_RangeMax: function(){
        return this.getHeight_Header()+this.height_hist_max+this.getHeight_Extra();
    },
    /** -- */
    getHeight_RangeMin: function(){
        return this.getHeight_Header()+this.height_hist_min+this.getHeight_Extra();
    },
    /** -- */
    isFiltered_min: function(){
        // the active min is different from intervalRange min.
        if(this.summaryFilter.active.min!==this.intervalRange.min) return true;
        // if using log scale, assume min is also filtered when max is filtered.
        if(this.scaleType==='log') return this.isFiltered_max();
        return false;
    },
    /** -- */
    isFiltered_max: function(){
        return this.summaryFilter.active.max!==this.intervalRange.max;
    },
    /** -- */
    getMaxAggr_Total: function(){
        return d3.max(this.histBins,function(aggr){ return aggr.length; });
    },
    /** -- */
    getMaxAggr_Active: function(){
        return d3.max(this.histBins,function(aggr){ return aggr.aggregate_Active; });
    },
    /** -- */
    initDOM: function(beforeDOM){
        this.initializeAggregates();
        if(this.isEmpty) return;
        if(this.DOM.inited===true) return;
        var me = this;

        this.insertRoot(beforeDOM);

        this.DOM.root
            .attr("hasMultiValueItem",false);

        this.insertHeader();

        this.DOM.wrapper = this.DOM.root.append("div").attr("class","wrapper");
        this.DOM.facetInterval = this.DOM.wrapper.append("div")
            .attr("class","facetInterval")
            .attr("scaleType",this.scaleType)
            .attr("zoomed",this.zoomed)
            .on("mousedown",function(){
                d3.event.stopPropagation();
                d3.event.preventDefault();
            });

        this.DOM.histogram = this.DOM.facetInterval.append("div").attr("class","histogram");
        this.DOM.histogram_bins = this.DOM.histogram.append("div").attr("class","bins")
            .style("margin-left",(this.width_vertAxisLabel)+"px");

        if(this.scaleType==='time'){
            this.DOM.timeSVG = this.DOM.histogram.append("svg").attr("class","timeSVG")
                .attr("xmlns","http://www.w3.org/2000/svg")
                .style("margin-left",(this.width_vertAxisLabel+this.width_barGap)+"px");
        }

        this.insertChartAxis_Measure(this.DOM.histogram, 'w', 'nw');
        this.DOM.chartAxis_Measure.style("padding-left",(this.width_vertAxisLabel-2)+"px")

        this.initDOM_Slider();

        if(this.showPercentile===true){
            this.initDOM_Percentile();
        }

        var _width_ = this.getWidth()-this.width_histMargin-this.width_vertAxisLabel;
        this.updateScaleAndBins( _width_, Math.ceil(_width_/this.optimumTickWidth));

        this.setCollapsed(this.collapsed);
        this.setUnitName(this.unitName);

        this.DOM.inited=true;
    },
    /** -- */
    setZoomed: function(v){
        this.zoomed = v;
        this.DOM.facetInterval.attr("zoomed",this.zoomed);
        if(this.zoomed){
            this.intervalRange.active.min = this.summaryFilter.active.min;
            this.intervalRange.active.max = this.summaryFilter.active.max;
            this.DOM.zoomControl.attr("sign","minus");
        } else {
            this.intervalRange.active.min = this.intervalRange.min;
            this.intervalRange.active.max = this.intervalRange.max;
            this.DOM.zoomControl.attr("sign","plus");
        }
        // TODO: enable this once all else is working...
        this.detectLogScale();
        var _width_ = this.getWidth()-this.width_histMargin-this.width_vertAxisLabel;
        this.updateScaleAndBins( _width_, Math.ceil(_width_/this.optimumTickWidth));
    },
    /** -- */
    setUnitName: function(v){
        this.unitName = v;
        this.refreshTickLabels();
    },
    /** -- */
    initDOM_Percentile: function(){
        var me=this;
        if(this.DOM.facetInterval===undefined) return;
        this.DOM.percentileGroup = this.DOM.facetInterval.append("div").attr("class","percentileGroup")
            .style('margin-left',this.width_vertAxisLabel+"px");;
        this.DOM.percentileGroup.append("span").attr("class","percentileTitle").html(kshf.lang.cur.Percentiles);

        this.DOM.quantile = {};

        [[10,90],[20,80],[30,70],[40,60]].forEach(function(qb){
            this.DOM.quantile[""+qb[0]+"_"+qb[1]] = this.DOM.percentileGroup.append("span")
                .attr("class","quantile q_range q_"+qb[0]+"_"+qb[1])
                .each(function(){
                    this.tipsy = new Tipsy(this, {
                        gravity: 's',
                        title: function(){
                            return "<span style='font-weight:300'>%"+qb[0]+" - %"+qb[1]+" Percentile: <span style='font-weight:500'>"+
                                me.quantile_val[qb[0]]+" - "+me.quantile_val[qb[1]]+"</span></span>"
                            ;
                        }
                    })
                })
                .on("mouseover",function(){ this.tipsy.show(); })
                .on("mouseout" ,function(){ this.tipsy.hide(); })
                ;
        },this);

        [10,20,30,40,50,60,70,80,90].forEach(function(q){
            this.DOM.quantile[q] = this.DOM.percentileGroup.append("span")
                .attr("class","quantile q_pos q_"+q)
                .each(function(){
                    this.tipsy = new Tipsy(this, {
                        gravity: 's',
                        title: function(){
                            return "Median: "+ me.quantile_val[q];
                        }
                    })
                })
                .on("mouseover",function(){ this.tipsy.show(); })
                .on("mouseout" ,function(){ this.tipsy.hide(); })
                ;
        },this);
    },
    /** -- */
    updateDOMwidth: function(){
        if(this.DOM.inited===false) return;
        var chartWidth = this.getWidth()-this.width_histMargin-this.width_vertAxisLabel;
        this.DOM.facetInterval.style("width",this.getWidth()+"px");
        this.DOM.summaryTitle.style("max-width",(this.getWidth()-40)+"px");
        if(this.DOM.timeSVG)
            this.DOM.timeSVG.style("width",(chartWidth+2)+"px")
    },
    /** --
        Uses
        - this.scaleType
        - this.intervalRange min & max
        Updates
        - this.intervalTickFormat
        - this.valueScale.nice()
        Return
        - the tick values in an array
      */
    getValueTicks: function(optimalTickCount){
        var me=this;
        var ticks;

        // HANDLE TIME CAREFULLY
        if(this.scaleType==='time') {
            // 1. Find the appropriate aggregation interval (day, month, etc)
            var timeRange_ms = this.intervalRange.active.max-this.intervalRange.active.min; // in milliseconds
            var timeInterval;
            var timeIntervalStep = 1;
            if((timeRange_ms/1000) < optimalTickCount){
                timeInterval = d3.time.second.utc;
                this.intervalTickFormat = d3.time.format.utc("%S");
            } else if((timeRange_ms/(1000*5)) < optimalTickCount){
                timeInterval = d3.time.second.utc;
                timeIntervalStep = 5;
                this.intervalTickFormat = d3.time.format.utc("%-S");
            } else if((timeRange_ms/(1000*15)) < optimalTickCount){
                timeInterval = d3.time.second.utc;
                timeIntervalStep = 15;
                this.intervalTickFormat = d3.time.format.utc("%-S");
            } else if((timeRange_ms/(1000*60)) < optimalTickCount){
                timeInterval = d3.time.minute.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = d3.time.format.utc("%-M");
            } else if((timeRange_ms/(1000*60*5)) < optimalTickCount){
                timeInterval = d3.time.minute.utc;
                timeIntervalStep = 5;
                this.intervalTickFormat = d3.time.format.utc("%-M");
            } else if((timeRange_ms/(1000*60*15)) < optimalTickCount){
                timeInterval = d3.time.minute.utc;
                timeIntervalStep = 15;
                this.intervalTickFormat = d3.time.format.utc("%-M");
            } else if((timeRange_ms/(1000*60*60)) < optimalTickCount){
                timeInterval = d3.time.hour.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = d3.time.format.utc("%-H");
            } else if((timeRange_ms/(1000*60*60*6)) < optimalTickCount){
                timeInterval = d3.time.hour.utc;
                timeIntervalStep = 6;
                this.intervalTickFormat = d3.time.format.utc("%-H");
            } else if((timeRange_ms/(1000*60*60*24)) < optimalTickCount){
                timeInterval = d3.time.day.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = d3.time.format.utc("%-e");
                // TODO: kshf.Util.ordinal_suffix_of();
            } else if((timeRange_ms/(1000*60*60*24*7)) < optimalTickCount){
                timeInterval = d3.time.week.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = function(v){
                    var suffix = kshf.Util.ordinal_suffix_of(v.getUTCDate());
                    var first=d3.time.format.utc("%-b")(v);
                    return suffix+"<br>"+first;
                };
                this.height_labels = 28;
            } else if((timeRange_ms/(1000*60*60*24*30)) < optimalTickCount){
                timeInterval = d3.time.month.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = function(v){
                    var threeMonthsLater = timeInterval.offset(v, 3);
                    var first=d3.time.format.utc("%-b")(v);
                    var s=first;
                    if(first==="Jan") s+="<br>"+(d3.time.format("%Y")(threeMonthsLater));
                    return s;
                };
                this.height_labels = 28;
            } else if((timeRange_ms/(1000*60*60*24*30*3)) < optimalTickCount){
                timeInterval = d3.time.month.utc;
                timeIntervalStep = 3;
                this.intervalTickFormat = function(v){
                    var threeMonthsLater = timeInterval.offset(v, 3);
                    var first=d3.time.format.utc("%-b")(v);
                    var s=first;
                    if(first==="Jan") s+="<br>"+(d3.time.format("%Y")(threeMonthsLater));
                    return s;
                };
                this.height_labels = 28;
            } else if((timeRange_ms/(1000*60*60*24*30*6)) < optimalTickCount){
                timeInterval = d3.time.month.utc;
                timeIntervalStep = 6;
                this.intervalTickFormat = function(v){
                    var threeMonthsLater = timeInterval.offset(v, 6);
                    var first=d3.time.format.utc("%-b")(v);
                    var s=first;
                    if(first==="Jan") s+="<br>"+(d3.time.format("%Y")(threeMonthsLater));
                    return s;
                };
                this.height_labels = 28;
            } else if((timeRange_ms/(1000*60*60*24*365)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 1;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else if((timeRange_ms/(1000*60*60*24*365*2)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 2;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else if((timeRange_ms/(1000*60*60*24*365*3)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 3;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else if((timeRange_ms/(1000*60*60*24*365*4)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 4;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else if((timeRange_ms/(1000*60*60*24*365*5)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 5;
                this.intervalTickFormat = function(v){
                    var later = timeInterval.offset(v, 4);
                    return d3.time.format.utc("%Y")(v);
                };
                this.height_labels = 28;
            } else if((timeRange_ms/(1000*60*60*24*365*25)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 25;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else if((timeRange_ms/(1000*60*60*24*365*100)) < optimalTickCount){
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 100;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            } else {
                timeInterval = d3.time.year.utc;
                timeIntervalStep = 500;
                this.intervalTickFormat = d3.time.format.utc("%Y");
            }

            this.valueScale.nice(timeInterval, timeIntervalStep);
            ticks = this.valueScale.ticks(timeInterval, timeIntervalStep);
        } else if(this.scaleType==='step'){
            ticks = [];
            for(var i=this.intervalRange.active.min ; i<=this.intervalRange.active.max; i++){
                ticks.push(i);
            }
            this.intervalTickFormat = d3.format("d");
        } else if(this.scaleType==='log'){
            this.valueScale.nice(optimalTickCount);
            // Generate ticks
            ticks = this.valueScale.ticks(optimalTickCount);
            while(ticks.length > optimalTickCount*1.6){
                ticks = ticks.filter(function(d,i){return i%2===0;});
            }
            if(!this.hasFloat)
                ticks = ticks.filter(function(d){return d%1===0;});
            this.intervalTickFormat = d3.format(".1s");
        } else {
            this.valueScale.nice(optimalTickCount);
            this.valueScale.nice(optimalTickCount);
            ticks = this.valueScale.ticks(optimalTickCount);
            this.valueScale.nice(optimalTickCount);
            ticks = this.valueScale.ticks(optimalTickCount);

            if(!this.hasFloat) ticks = ticks.filter(function(d){return d===0||d%1===0;});

            var d3Formating = d3.format(this.hasFloat?".2f":".2s");
            this.intervalTickFormat = function(d){
                if(!me.hasFloat && d<10) return d;
                if(!me.hasFloat && Math.abs(ticks[1]-ticks[0])<1000) return d;
                var x= d3Formating(d);
                if(x.indexOf(".00")!==-1) x = x.replace(".00","");
                if(x.indexOf(".0")!==-1) x = x.replace(".0","");
                return x;
            }
        }

        return ticks;
    },
    /**
      Uses
      - optimumTickWidth
      - this.intervalRang
      Updates:
      - scaleType (if steps is more appropriate)
      - valueScale
      - intervalTickFormat
      */
    updateScaleAndBins: function(_width_,optimalTickCount){
        if(this.isEmpty) return;
        var me=this;

        // Check if you can use a ste-scale instead
        var stepRange=(this.intervalRange.active.max-this.intervalRange.active.min)+1;
        var stepWidth=_width_/stepRange;
        if(!this.hasFloat && (this.scaleType==='step' || this.scaleType==='linear')) {
            if(optimalTickCount>=stepRange){
                this.setScaleType('step');
            } else {
                this.setScaleType('linear');
            }
        }

        // UPDATE intervalScale
        switch(this.scaleType){
            case 'linear': case 'step':
                this.valueScale = d3.scale.linear();      break;
            case 'log':
                this.valueScale = d3.scale.log().base(2); break;
            case 'time':
                this.valueScale = d3.time.scale.utc();    break;
        }

        this.valueScale
            .domain([this.intervalRange.active.min, this.intervalRange.active.max])
            .range([0, _width_]);

        if(this.scaleType==='step'){
            this.valueScale.range([stepWidth/2, _width_-stepWidth/2]);
        }

        var ticks = this.getValueTicks(optimalTickCount);

        // Sometimes, the number of bins generated is larger than the optimal
        // In some cases, the ticks become suitable for step-scale. Detect it here.
        if(!this.hasFloat && (this.scaleType==='step' || this.scaleType==='linear')){
            if(ticks.length===stepRange){
                this.setScaleType('step');
                this.valueScale.range([stepWidth/2, _width_-stepWidth/2]);
            }
        }

        if(this.scaleType!=='step'){
            this.aggrWidth = this.valueScale(ticks[1])-this.valueScale(ticks[0]);
        } else {
            this.aggrWidth = _width_/stepRange;
        }

        var ticksChanged = (this.intervalTicks.length!==ticks.length) ||
            this.intervalTicks[0]!==ticks[0] ||
            this.intervalTicks[this.intervalTicks.length-1] !== ticks[ticks.length-1]
            ;

        if(ticksChanged){
            this.intervalTicks = ticks;
            var filterId = this.summaryFilter.id;

            var itemV = function(item){
                // if(item.isWanted)  // Include all items - Aggregate also shows the "total" viz
                    return item.mappedDataCache[filterId].v;
            };
            if(this.zoomed===false){
                itemV = this.itemV;
            }
            if(this.scaleType!=='step'){
                this.histBins = d3.layout.histogram().bins(this.intervalTicks).value(itemV)(this.filteredItems);
            } else {
                // I'll do the bins myself, d3 just messes it up when I need a simple step scale
                this.histBins = [];
                for(var bin=this.intervalRange.active.min; bin<=this.intervalRange.active.max; bin++){
                    var d = [];
                    d.x = bin;
                    d.y = 0;
                    d.dx = 0;
                    this.histBins.push(d);
                }
                this.filteredItems.forEach(function(item){
                    var v = itemV(item);
                    if(v===null || v===undefined) return;
                    if(v<this.intervalRange.active.min) return;
                    if(v>this.intervalRange.active.max) return;
                    var bin = this.histBins[v-this.intervalRange.active.min];
                    bin.push(item);
                    bin.y++;
                },this);
            }

            this.updateAggregate_Active();
            this.updateBarScale2Active();

            if(this.DOM.root){
                this.insertVizDOM();
            }

            if(this.showPercentile) this.updatePercentiles();
        }
        if(this.DOM.root){
            if(this.DOM.aggr_Group===undefined){
                this.insertVizDOM();
            }
            this.refreshBins_Translate();
            this.refreshViz_Scale();

            this.DOM.labelGroup.selectAll(".tick").style("left",function(d){
                return (me.valueScale(d))+"px";
            });
            this.refreshIntervalSlider();
        }
    },
    /** -- */
    insertVizDOM: function(){
        if(this.scaleType==='time' && this.DOM.root) {
            // delete existing DOM:
            // TODO: Find  a way to avoid this?
            this.DOM.timeSVG.select(".lineTrend.total").remove();
            this.DOM.timeSVG.select(".lineTrend.active").remove();
            this.DOM.timeSVG.select(".lineTrend.preview").remove();
            this.DOM.timeSVG.select(".lineTrend.compare").remove();
            this.DOM.timeSVG.selectAll("line.activeLine").remove();
            this.DOM.timeSVG.selectAll("line.previewLine").remove();
            this.DOM.timeSVG.selectAll("line.compareLine").remove();

            this.DOM.lineTrend_Total = this.DOM.timeSVG.append("path").attr("class","lineTrend total")
                .datum(this.histBins);
            this.DOM.lineTrend_Active = this.DOM.timeSVG.append("path").attr("class","lineTrend active")
                .datum(this.histBins);
            this.DOM.lineTrend_ActiveLine = this.DOM.timeSVG.selectAll("line.activeLine")
                .data(this.histBins, function(d,i){ return i; })
                .enter().append("line").attr("class","lineTrend activeLine");
            this.DOM.lineTrend_Preview = this.DOM.timeSVG.append("path").attr("class","lineTrend preview")
                .datum(this.histBins);
            this.DOM.lineTrend_PreviewLine = this.DOM.timeSVG.selectAll("line.previewLine")
                .data(this.histBins, function(d,i){ return i; })
                .enter().append("line").attr("class","lineTrend previewLine");
            this.DOM.lineTrend_Compare = this.DOM.timeSVG.append("path").attr("class","lineTrend compare")
                .datum(this.histBins);
            this.DOM.lineTrend_CompareLine = this.DOM.timeSVG.selectAll("line.compareLine")
                .data(this.histBins, function(d,i){ return i; })
                .enter().append("line").attr("class","lineTrend compareLine");
        }

        this.insertBins();
        this.refreshViz_Axis();
        //this.refreshViz_Preview();
        this.refreshMeasureLabel();
        this.updateTicks();
    },
    /** -- */
    updateTicks: function(){
        this.DOM.labelGroup.selectAll(".tick").data([]).exit().remove(); // remove all existing ticks
        var ddd = this.DOM.labelGroup.selectAll(".tick").data(this.intervalTicks);
        var ddd_enter = ddd.enter().append("span").attr("class","tick");
            ddd_enter.append("span").attr("class","line");
            ddd_enter.append("span").attr("class","text");
        this.refreshTickLabels();
    },
    /** -- */
    getBarWidth: function(){
        return this.aggrWidth - this.width_barGap*2;
    },
    /** -- */
    refreshTickLabels: function(){
        var me=this;
        if(this.DOM.labelGroup===undefined) return;
        this.DOM.labelGroup.selectAll(".tick .text").html(function(d){
            if(me.scaleType==='time'){
                 return me.intervalTickFormat(d);
            } else {
                var v;
                if(d<1 && d!==0) v=d.toFixed(1);
                else v=me.intervalTickFormat(d);

                if(me.unitName) v+="<span class='unitName'>"+me.unitName+"</span>";
                return v;
            }
        });
    },
    /** -- */
    insertBins: function(){
        var me=this;
        var resultPreviewLogTimeout = null;

        var filterId = this.summaryFilter.id;

        // just remove everything that was in the histogram_bins befoe
        this.DOM.histogram_bins
            .selectAll(".aggr_Group").data([]).exit().remove();

        var activeBins = this.DOM.histogram_bins
            .selectAll(".aggr_Group").data(this.histBins, function(d,i){ return i; });

        var newBins=activeBins.enter().append("span").attr("class","aggr_Group")
            .each(function(aggr){
                aggr.aggregate_Preview=0;
                aggr.forEach(function(item){
                    item.mappedDataCache[filterId].b = aggr;
                },this);
                aggr.DOM = {}
                aggr.DOM.facet = this;
            })
            .on("mouseenter",function(aggr){
                var thiss=this;

                me.browser.previewedSelectionSummary = me;

                if(!me.browser.pauseResultPreview){
                    var timeoutTime = kshf.previewTimeoutMS;
                    if(me.browser.vizCompareActive) timeoutTime = 0;
//                    this.resultPreviewShowTimeout = setTimeout(function(){
                        aggr.forEach(function(item){item.updatePreview(me.parentFacet);});
                        me.browser.itemCount_Previewed = aggr.aggregate_Preview;
                        // Histograms cannot have sub-facets, so don't iterate over mappedDOMs...
                        thiss.setAttribute("highlight","selected");
                        thiss.setAttribute("showlock",true);
                        me.browser.refreshResultPreviews();
                        if(sendLog) {
                            if(resultPreviewLogTimeout){
                                clearTimeout(resultPreviewLogTimeout);
                            }
                            resultPreviewLogTimeout = setTimeout(function(){
                                sendLog(kshf.LOG.FILTER_PREVIEW, {id:me.summaryFilter.id, info: aggr.x+"x"+aggr.dx});
                            }, 1000); // wait 1 second to see the update fully
                        }
//                    },timeoutTime);
                }
            })
            .on("mouseleave",function(aggr){
                me.browser.previewedSelectionSummary = null;

                if(resultPreviewLogTimeout){
                    clearTimeout(resultPreviewLogTimeout);
                }
                if(this.resultPreviewShowTimeout){
                    clearTimeout(this.resultPreviewShowTimeout);
                    this.resultPreviewShowTimeout = null;
                }
                if(!me.browser.pauseResultPreview){
                    this.setAttribute("highlight",false);
                    this.setAttribute("showlock",false);

                    me.browser.items.forEach(function(item){
                        if(item.DOM.record) item.DOM.record.setAttribute("highlight",false);
                    })
                    me.browser.clearResultPreviews();
                }
            })
            .on("click",function(aggr){
                if(me.summaryFilter.filteredBin===this){
                    me.summaryFilter.clearFilter();
                    return;
                }
                this.setAttribute("filtered","true");

                // store histogram state
                me.summaryFilter.dom_HistogramBar = this;
                if(me.scaleType!=='time'){
                    me.summaryFilter.active = {
                        min: aggr.x,
                        max: aggr.x+aggr.dx
                    };
                } else {
                    me.summaryFilter.active = {
                        min: aggr.x,
                        max: new Date(aggr.x.getTime()+aggr.dx)
                    };
                }
                // if we are filtering the last aggr, make max_score inclusive
                me.summaryFilter.max_inclusive = (aggr.x+aggr.dx)===me.intervalRange.active.max;
                if(me.scaleType==='step'){
                    me.summaryFilter.max_inclusive = true;
                }

                me.summaryFilter.filteredBin=this;
                me.summaryFilter.addFilter(true);
                if(sendLog) sendLog(kshf.LOG.FILTER_INTRVL_BIN,
                    {id:me.summaryFilter.id, info:me.summaryFilter.active.min+"x"+me.summaryFilter.active.max} );
            });

        newBins.append("span").attr("class","aggr total");
        newBins.append("span").attr("class","aggr total_tip");
        newBins.append("span").attr("class","aggr active");
        newBins.append("span").attr("class","aggr preview").attr("fast",true);
        newBins.append("span").attr("class","aggr compare").attr("hidden",true);

        newBins.append("span").attr("class","compareButton fa")
            .each(function(aggr){
                this.tipsy = new Tipsy(this, {
                    gravity: 's',
                    title: function(){
                        return (me.browser.comparedAggregate!==aggr)?
                            kshf.lang.cur.LockToCompare:kshf.lang.cur.Unlock;
                    }
                });
            })
            .on("click",function(aggr){
                this.tipsy.hide();
                me.browser.setPreviewCompare(aggr);
                d3.event.stopPropagation();
            })
            .on("mouseenter",function(aggr){
                this.tipsy.options.className = "tipsyFilterLock";
                this.tipsy.hide();
                this.tipsy.show();
                d3.event.stopPropagation();
            })
            .on("mouseleave",function(aggr){
                this.tipsy_title = undefined;
                this.tipsy.hide();
                d3.event.stopPropagation();
            })
            ;

        newBins.append("span").attr("class","measureLabel").each(function(bar){
            kshf.Util.setTransform(this,"translateY("+me.height_hist+"px)");
        });

        this.DOM.aggr_Group    = this.DOM.histogram_bins.selectAll(".aggr_Group");
        this.DOM.aggr_Total    = this.DOM.aggr_Group.selectAll(".total");
        this.DOM.aggr_TotalTip = this.DOM.aggr_Group.selectAll(".total_tip");
        this.DOM.aggr_Active   = this.DOM.aggr_Group.selectAll(".active");
        this.DOM.aggr_Preview  = this.DOM.aggr_Group.selectAll(".preview");
        this.DOM.aggr_Compare  = this.DOM.aggr_Group.selectAll(".compare");

        this.DOM.compareButton = this.DOM.aggr_Group.selectAll(".compareButton");
        this.DOM.measureLabel  = this.DOM.aggr_Group.selectAll(".measureLabel");
    },
    /** --- */
    roundFilterRange: function(){
        // Make sure the range is within the visible limits:
        this.summaryFilter.active.min = Math.max(
            this.intervalTicks[0], this.summaryFilter.active.min);
        this.summaryFilter.active.max = Math.min(
            this.intervalTicks[this.intervalTicks.length-1], this.summaryFilter.active.max);

        if(this.scaleType==='time'){
            // TODO: Round to meaningful dates
            return;
        }
        if(this.scaleType==='log' || this.scaleType==='step' || (!this.hasFloat) ){
            this.summaryFilter.active.min=Math.round(this.summaryFilter.active.min);
            this.summaryFilter.active.max=Math.round(this.summaryFilter.active.max);
        }
    },
    /** -- */
    initDOM_Slider: function(){
        var me=this;

        this.DOM.intervalSlider = this.DOM.facetInterval.append("div").attr("class","intervalSlider")
            .style('margin-left',(this.width_vertAxisLabel)+"px");

        this.DOM.zoomControl = this.DOM.intervalSlider.append("span").attr("class","zoomControl fa")
            .attr("sign","plus")
            .each(function(d){
                this.tipsy = new Tipsy(this, {
                    gravity: 'w', title: function(){
                        return (this.getAttribute("sign")==="plus")?"Zoom into range":"Zoom out";
                    }
                });
            })
            .on("mouseenter",function(){ this.tipsy.show(); })
            .on("mouseleave",function(){ this.tipsy.hide(); })
            .on("click",function(){
                this.tipsy.hide();
                me.setZoomed(this.getAttribute("sign")==="plus");
            })
            ;

        var controlLine = this.DOM.intervalSlider.append("div").attr("class","controlLine")
            .on("mousedown", function(){
                if(d3.event.which !== 1) return; // only respond to left-click
                me.browser.setNoAnim(true);
                var e=this.parentNode;
                var initPos = me.valueScale.invert(d3.mouse(e)[0]);
                d3.select("body").style('cursor','ew-resize')
                    .on("mousemove", function() {
                        var targetPos = me.valueScale.invert(d3.mouse(e)[0]);
                        me.summaryFilter.active.min=d3.min([initPos,targetPos]);
                        me.summaryFilter.active.max=d3.max([initPos,targetPos]);
                        me.roundFilterRange();
                        me.refreshIntervalSlider();
                        // wait half second to update
                        if(this.timer){
                            clearTimeout(this.timer);
                            this.timer = null;
                        }
                        me.summaryFilter.filteredBin=this;
                        this.timer = setTimeout(function(){
                            if(me.isFiltered_min() || me.isFiltered_max()){
                                me.summaryFilter.addFilter(true);
                                if(sendLog) sendLog(kshf.LOG.FILTER_INTRVL_HANDLE,
                                    { id: me.summaryFilter.id,
                                      info: me.summaryFilter.active.min+"x"+me.summaryFilter.active.m});
                            } else {
                                me.summaryFilter.clearFilter();
                            }
                        },250);
                    }).on("mouseup", function(){
                        me.browser.setNoAnim(false);
                        d3.select("body").style('cursor','auto').on("mousemove",null).on("mouseup",null);
                    });
                d3.event.preventDefault();
            });

        controlLine.append("span").attr("class","base total");
        controlLine.append("span").attr("class","base active")
            .each(function(){
                this.tipsy = new Tipsy(this, {
                    gravity: "s",
                    title: function(){ return kshf.lang.cur.DragToFilter; }
                })
            })
            // TODO: The problem is, the x-position (left-right) of the tooltip is not correctly calculated
            // because the size of the bar is set by scaling, not through width....
            //.on("mouseover",function(){ this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(){
                this.tipsy.hide();
                if(d3.event.which !== 1) return; // only respond to left-click
                if(me.scaleType==='time') return; // time is not supported for now.
                me.browser.setNoAnim(true);
                var e=this.parentNode;
                var initMin = me.summaryFilter.active.min;
                var initMax = me.summaryFilter.active.max;
                var initRange= initMax - initMin;
                var initPos = d3.mouse(e)[0];

                d3.select("body").style('cursor','ew-resize')
                    .on("mousemove", function() {
                        if(me.scaleType==='log'){
                            var targetDif = d3.mouse(e)[0]-initPos;
                            me.summaryFilter.active.min =
                                me.valueScale.invert(me.valueScale(initMin)+targetDif);
                            me.summaryFilter.active.max =
                                me.valueScale.invert(me.valueScale(initMax)+targetDif);

                        } else {
                            var targetPos = me.valueScale.invert(d3.mouse(e)[0]);
                            var targetDif = targetPos-me.valueScale.invert(initPos);

                            me.summaryFilter.active.min = initMin+targetDif;
                            me.summaryFilter.active.max = initMax+targetDif;
                            if(me.summaryFilter.active.min<me.intervalRange.active.min){
                                me.summaryFilter.active.min=me.intervalRange.active.min;
                                me.summaryFilter.active.max=me.intervalRange.active.min+initRange;
                            }
                            if(me.summaryFilter.active.max>me.intervalRange.active.max){
                                me.summaryFilter.active.max=me.intervalRange.active.max;
                                me.summaryFilter.active.min=me.intervalRange.active.max-initRange;
                            }
                        }

                        me.roundFilterRange();
                        me.refreshIntervalSlider();

                        // wait half second to update
                        if(this.timer){
                            clearTimeout(this.timer);
                            this.timer = null;
                        }
                        me.summaryFilter.filteredBin = this;
                        this.timer = setTimeout(function(){
                            if(me.isFiltered_min() || me.isFiltered_max()){
                                me.summaryFilter.addFilter(true);
                                if(sendLog) sendLog(kshf.LOG.FILTER_INTRVL_HANDLE,
                                    { id: me.summaryFilter.id,
                                      info: me.summaryFilter.active.min+"x"+me.summaryFilter.active.max});
                            } else{
                                me.summaryFilter.clearFilter();
                            }
                        },200);
                    }).on("mouseup", function(){
                        me.browser.setNoAnim(false);
                        d3.select("body").style('cursor','auto').on("mousemove",null).on("mouseup",null);
                    });
                d3.event.preventDefault();
                d3.event.stopPropagation();
            });

        var handle_cb = function (d, i) {
            var mee = this;
            if(d3.event.which !== 1) return; // only respond to left-click
            me.browser.setNoAnim(true);
            var e=this.parentNode;
            d3.select("body").style('cursor','ew-resize')
                .on("mousemove", function() {
                    mee.dragging = true;
                    me.browser.pauseResultPreview = true;
                    var targetPos = me.valueScale.invert(d3.mouse(e)[0]);
                    me.summaryFilter.active[d] = targetPos;
                    // Swap is min > max
                    if(me.summaryFilter.active.min>me.summaryFilter.active.max){
                        var t=me.summaryFilter.active.min;
                        me.summaryFilter.active.min = me.summaryFilter.active.max;
                        me.summaryFilter.active.max = t;
                        if(d==='min') d='max'; else d='min';
                    }
                    me.roundFilterRange();
                    me.refreshIntervalSlider();
                    // wait half second to update
                    if(this.timer){
                        clearTimeout(this.timer);
                        this.timer = null;
                    }
                    me.summaryFilter.filteredBin=this;
                    this.timer = setTimeout( function(){
                        if(me.isFiltered_min() || me.isFiltered_max()){
                            if(sendLog) sendLog(kshf.LOG.FILTER_INTRVL_HANDLE,
                                { id: me.summaryFilter.id,
                                  info: me.summaryFilter.active.min+"x"+me.summaryFilter.active.max });
                            me.summaryFilter.addFilter(true);
                        } else {
                            me.summaryFilter.clearFilter();
                        }
                    },200);
                }).on("mouseup", function(){
                    mee.dragging = false;
                    me.browser.pauseResultPreview = false;
                    me.browser.setNoAnim(false);
                    d3.select("body").style('cursor','auto').on("mousemove",null).on("mouseup",null);
                });
            d3.event.preventDefault();
            d3.event.stopPropagation();
        };

        controlLine.selectAll(".handle").data(['min','max']).enter()
            .append("span").attr("class",function(d){ return "handle "+d; })
            .each(function(d,i){
                this.tipsy = new Tipsy(this, {
                    gravity: i==0?"e":"w", title: function(){ return kshf.lang.cur.DragToFilter }
                })
            })
            .on("mouseover",function(){ if(this.dragging!==true) this.tipsy.show(); })
            .on("mouseout" ,function(){ this.tipsy.hide(); })
            .on("mousedown", function(d,i){
                this.tipsy.hide();
                handle_cb.call(this,d,i);
            })
            .append("span").attr("class","rangeLimitOnChart");

        this.DOM.selectedItemValue = controlLine.append("div").attr("class","selectedItemValue");
        this.DOM.selectedItemValue.append("span").attr("class","circlee");
        this.DOM.selectedItemValueText = this.DOM.selectedItemValue
            .append("span").attr("class","selected-item-value-text")
            .append("span").attr("class","selected-item-value-text-v");

        this.DOM.labelGroup = this.DOM.intervalSlider.append("div").attr("class","labelGroup");
    },
    /** -- */
    updateBarScale2Total: function(){
        this.chartScale_Measure
            .domain([0, this.getMaxAggr_Total()])
            .range ([0, this.height_hist]);
    },
    /** -- */
    updateBarScale2Active: function(){
        this.chartScale_Measure
            .domain([0, this.getMaxAggr_Active()])
            .range ([0, this.height_hist]);
    },
    /** -- */
    updateAggregate_Active: function(){
        this.histBins.forEach(function(aggr){ aggr.aggregate_Active = 0; });

        if(this.parentFacet && this.parentFacet.hasCategories()){
            this.histBins.forEach(function(aggr){
                aggr.forEach(function(item){
                    if(item.aggregate_Active>0) aggr.aggregate_Active+=item.aggregate_Self;
                });
            });
        } else {
            this.histBins.forEach(function(aggr){
                aggr.forEach(function(item){ if(item.isWanted) aggr.aggregate_Active+=item.aggregate_Self; });
            });
        }
    },
    /** -- */
    refreshBins_Translate: function(){
        var me=this;
        var offset = 0;
        if(this.scaleType==='step') offset = this.width_barGap-this.aggrWidth/2;
        if(this.scaleType==='time') offset = this.width_barGap;
        this.DOM.aggr_Group
            .style("width",this.getBarWidth()+"px")
            .each(function(aggr){
                kshf.Util.setTransform(this,"translateX("+(me.valueScale(aggr.x)+offset)+"px)");
            });
    },
    /** -- Note: Same as the function used for categorical facet */
    refreshViz_All: function(){
        if(this.isEmpty || this.collapsed) return;
        var me=this;
        this.refreshViz_Total();
        this.refreshViz_Active();

        this.DOM.aggr_Preview.attr("fast",null); // take it slow for result preview animations
        this.refreshViz_Preview();
        setTimeout(function(){ me.DOM.aggr_Preview.attr("fast",true); },800);

        this.refreshViz_Compare();
        this.refreshMeasureLabel();
        this.refreshViz_Axis();
    },
    /** -- */
    refreshViz_Scale: function(){
        this.refreshViz_Total();
        this.refreshViz_Active();
    },
    /** -- */
    refreshViz_Total: function(){
        if(this.isEmpty || this.collapsed) return;
        var me=this;
        var width=this.getBarWidth();

        var heightTotal = function(aggr){
            if(aggr.length===0) return 0;
            if(me.browser.ratioModeActive) return me.height_hist;
            return me.chartScale_Measure(aggr.length);
        };

        if(this.scaleType==='time'){
            var durationTime=this.browser.noAnim?0:700;
            this.timeSVGLine = d3.svg.area()
                .x(function(aggr){
                    return me.valueScale(aggr.x)+width/2;
                })
                .y0(me.height_hist)
                .y1(function(aggr){
                    if(aggr.aggregate_Total===0) return me.height_hist+3;
                    return me.height_hist-heightTotal(aggr);
                });
            this.DOM.lineTrend_Total
                .transition().duration(durationTime)
                .attr("d", this.timeSVGLine);
        } else {
            this.DOM.aggr_Total.each(function(aggr){
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) scale("+width+","+heightTotal(aggr)+")");
            });
            if(!this.browser.ratioModeActive){
                this.DOM.aggr_TotalTip
                    .style("opacity",function(aggr){
                        return (aggr.length>me.chartScale_Measure.domain()[1])?1:0;
                    })
                    .style("width",width+"px");
            } else {
                this.DOM.aggr_TotalTip.style("opacity",0);
            }
        }
    },
    /** -- */
    refreshViz_Active: function(){
        if(this.isEmpty || this.collapsed) return;
        var me=this;
        var width = this.getBarWidth();

        var heightActive = function(aggr){
            if(aggr.aggregate_Active===0) return 0;
            if(me.browser.ratioModeActive) return me.height_hist;
            return me.chartScale_Measure(aggr.aggregate_Active);
        };

        if(!this.isFiltered() || this.scaleType==='step'){
            this.DOM.aggr_Active.each(function(aggr){
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) scale("+width+","+heightActive(aggr)+")");
            });
        } else {
            // is filtered & not step scale
            var filter_min = this.summaryFilter.active.min;
            var filter_max = this.summaryFilter.active.max;
            var minPos = this.valueScale(filter_min);
            var maxPos = this.valueScale(filter_max);
            this.DOM.aggr_Active.each(function(aggr){
                var translateX = "";
                var width_self=width;
                var aggr_min = aggr.x;
                var aggr_max = aggr.x + aggr.dx;
                if(aggr.aggregate_Active>0){
                    // it is within the filtered range
                    if(aggr_min<filter_min){
                        var lostWidth = minPos-me.valueScale(aggr_min);
                        translateX = "translateX("+lostWidth+"px) ";
                        width_self -= lostWidth;
                    }
                    if(aggr_max>filter_max){
                        var lostWidth = me.valueScale(aggr_max)-maxPos-me.width_barGap*2;
                        //translateX = " translateX("+lostWidth+"px)";
                        width_self -= lostWidth;
                    }
                }
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) "+translateX+"scale("+width_self+","+heightActive(aggr)+")");
            });
        }

        this.DOM.compareButton
            .each(function(aggr){
                kshf.Util.setTransform(this,"translateY("+(me.height_hist-heightActive(aggr)-9)+"px)");
            })
            .attr("inside",function(aggr){
                if(me.browser.ratioModeActive) return "";
                if(me.height_hist-heightActive(aggr)<6) return "";
            });

        if(this.scaleType==='time'){
            var durationTime=this.browser.noAnim?0:700;
            this.timeSVGLine = d3.svg.area()
                .x(function(aggr){
                    return me.valueScale(aggr.x)+width/2;
                })
                .y0(me.height_hist+2)
                .y1(function(aggr){
                    if(aggr.aggregate_Active===0) return me.height_hist+3;
                    return me.height_hist-heightActive(aggr);
                });

            this.DOM.lineTrend_Active
              .transition().duration(durationTime)
              .attr("d", this.timeSVGLine);

            this.DOM.lineTrend_ActiveLine.transition().duration(durationTime)
                .attr("y1",function(aggr){ return me.height_hist+3; })
                .attr("y2",function(aggr){
                    if(aggr.aggregate_Active===0) return me.height_hist+3;
                    return me.height_hist-heightActive(aggr);
                })
                .attr("x1",function(aggr){
                    return me.valueScale(aggr.x)+width/2;
                })
                .attr("x2",function(aggr){ return me.valueScale(aggr.x)+width/2; });
        }
    },
    /** Gets the active previewed value, and stores it in the cache */
    cachePreviewValue: function(){
        if(this.isEmpty || this.collapsed) return;
        var preview_not=this.browser.preview_not;
        this.histBins.forEach(function(aggr){
            aggr.aggregate_Compare = aggr.aggregate_Preview;
            if(preview_not) {
                aggr.aggregate_Compare = aggr.aggregate_Active-aggr.aggregate_Preview;
            }
        });
    },
    /** -- */
    refreshViz_Compare: function(){
        if(this.isEmpty || this.collapsed) return;
        if(!this.browser.vizCompareActive) return;

        var me=this;
        var width = this.getBarWidth();

        var heightCompare = function(aggr){
            if(aggr.aggregate_Compare===0) return 0;
            if(me.browser.ratioModeActive)
                return (aggr.aggregate_Compare/aggr.aggregate_Active)*me.height_hist;
            return me.chartScale_Measure(aggr.aggregate_Compare);
        };

        if(!this.isFiltered() || this.scaleType==='step'){
            this.DOM.aggr_Compare.each(function(aggr){
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) scale("+(width/2)+","+heightCompare(aggr)+")");
            });
        } else {
            // is filtered & not step scale
            var filter_min = this.summaryFilter.active.min;
            var filter_max = this.summaryFilter.active.max;
            var minPos = this.valueScale(filter_min);
            var maxPos = this.valueScale(filter_max);
            this.DOM.aggr_Compare.each(function(aggr){
                var translateX = "";
                var width_self=width;
                var aggr_min = aggr.x;
                var aggr_max = aggr.x + aggr.dx;
                if(aggr.aggregate_Active>0){
                    // it is within the filtered range
                    if(aggr_min<filter_min){
                        var lostWidth = minPos-me.valueScale(aggr_min);
                        translateX = "translateX("+lostWidth+"px) ";
                        width_self -= lostWidth;
                    }
                    if(aggr_max>filter_max){
                        var lostWidth = me.valueScale(aggr_max)-maxPos-me.width_barGap*2;
                        //translateX = " translateX("+lostWidth+"px)";
                        width_self -= lostWidth;
                    }
                }
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) "+translateX+"scale("+(width_self/2)+","+heightCompare(aggr)+")");
            });
        }

        if(this.scaleType==='time'){
            this.timeSVGLine = d3.svg.line()
                .x(function(aggr){  return me.valueScale(aggr.x)+width/2; })
                .y(function(aggr){
                    if(aggr.aggregate_Compare===0) return me.height_hist+3;
                    return me.height_hist-heightCompare(aggr);
                });

            var durationTime=0;
            if(this.browser.vizCompareActive){
                durationTime=200;
            }

            this.DOM.lineTrend_Compare
                .transition()
                .duration(durationTime)
                .attr("d", this.timeSVGLine);

            this.DOM.lineTrend_CompareLine.transition().duration(durationTime)
                .attr("y1",function(aggr){ return me.height_hist+3; })
                .attr("y2",function(aggr){
                    if(aggr.aggregate_Compare===0) return me.height_hist+3;
                    return me.height_hist-heightCompare(aggr);
                })
                .attr("x1",function(aggr){
                    return me.valueScale(aggr.x)+width/2+1;
                })
                .attr("x2",function(aggr){ return me.valueScale(aggr.x)+width/2+1; });
        }
    },
    /** -- */
    refreshViz_Preview: function(){
        if(this.isEmpty || this.collapsed) return;
        var me=this;
        var width = this.getBarWidth();

        var getAggrHeight_Preview = function(aggr){
            var p=aggr.aggregate_Preview;
            if(me.browser.preview_not) p = aggr.aggregate_Active-aggr.aggregate_Preview;
            if(me.browser.ratioModeActive){
                if(aggr.aggregate_Active===0) return 0;
                return (p / aggr.aggregate_Active)*me.height_hist;
            } else {
                return me.chartScale_Measure(p);
            }
        };

        if(!this.isFiltered() || this.scaleType==='step'){
            this.DOM.aggr_Preview.each(function(aggr){
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) scale("+width+","+getAggrHeight_Preview(aggr)+")");
            });
        } else {
            // is filtered & not step scale
            var filter_min = this.summaryFilter.active.min;
            var filter_max = this.summaryFilter.active.max;
            var minPos = this.valueScale(filter_min);
            var maxPos = this.valueScale(filter_max);
            this.DOM.aggr_Preview.each(function(aggr){
                var translateX = "";
                var width_self=width;
                var aggr_min = aggr.x;
                var aggr_max = aggr.x + aggr.dx;
                if(aggr.aggregate_Active>0){
                    // it is within the filtered range
                    if(aggr_min<filter_min){
                        var lostWidth = minPos-me.valueScale(aggr_min);
                        translateX = "translateX("+lostWidth+"px) ";
                        width_self -= lostWidth;
                    }
                    if(aggr_max>filter_max){
                        var lostWidth = me.valueScale(aggr_max)-maxPos-me.width_barGap*2;
                        //translateX = " translateX("+lostWidth+"px)";
                        width_self -= lostWidth;
                    }
                }
                kshf.Util.setTransform(this,
                    "translateY("+me.height_hist+"px) "+translateX+"scale("+width_self+","+getAggrHeight_Preview(aggr)+")");
            });
        }

        this.refreshMeasureLabel();

        if(this.scaleType==='time'){
            var durationTime=200;
            this.timeSVGLine = d3.svg.area()
                .x(function(aggr){
                    return me.valueScale(aggr.x)+width/2;
                })
                .y0(me.height_hist+2)
                .y1(function(aggr){
                    if(aggr.aggregate_Preview===0) return me.height_hist+3;
                    return me.height_hist-getAggrHeight_Preview(aggr);
                });

            this.DOM.lineTrend_Preview
                .transition().duration(durationTime)
                .attr("d", this.timeSVGLine);

            this.DOM.lineTrend_PreviewLine.transition().duration(durationTime)
                .attr("y1",function(aggr){ return me.height_hist+3; })
                .attr("y2",function(aggr){
                    if(aggr.aggregate_Preview===0) return me.height_hist+3;
                    return me.height_hist-getAggrHeight_Preview(aggr);
                })
                .attr("x1",function(aggr){
                    return me.valueScale(aggr.x)+width/2-1;
                })
                .attr("x2",function(aggr){ return me.valueScale(aggr.x)+width/2-1; });
        }
    },
    /** -- */
    clearViz_Preview: function(){
        if(this.isEmpty || this.collapsed) return;
        if(this.DOM.aggr_Preview===undefined) return;
        var me=this;
        var width = this.getBarWidth();
        var transform="translateY("+this.height_hist+"px) "+"scale("+this.getBarWidth()+",0)";
        this.DOM.aggr_Preview.each(function(bar){
            bar.aggregate_Preview=0;
            kshf.Util.setTransform(this,transform);
        });
        this.refreshMeasureLabel();

        if(this.scaleType==='time'){
            var durationTime=200;
            this.timeSVGLine = d3.svg.line()
                .x(function(aggr){
                    return me.valueScale(aggr.x)+width/2;
                })
                .y(function(aggr){
                    return me.height_hist;
                });

            this.DOM.lineTrend_Preview
                .transition().duration(durationTime)
                .attr("d", this.timeSVGLine);
        }
    },
    /** -- */
    refreshViz_Axis: function(){
        if(this.isEmpty || this.collapsed) return;
        var me = this, tickValues, maxValue;

        var chartAxis_Measure_TickSkip = me.height_hist/17;

        if(this.browser.ratioModeActive) {
            maxValue = 100;
            tickValues = d3.scale.linear()
                .rangeRound([0, this.height_hist])
                .domain([0,100])
                .ticks(chartAxis_Measure_TickSkip)
                .filter(function(d){return d!==0;});
        } else {
            if(this.browser.percentModeActive) {
                maxValue = Math.round(100*me.getMaxAggr_Active()/me.browser.itemsWantedCount);
                tickValues = d3.scale.linear()
                    .rangeRound([0, this.height_hist])
                    .nice(chartAxis_Measure_TickSkip)
                    .clamp(true)
                    .domain([0,maxValue])
                    .ticks(chartAxis_Measure_TickSkip);
            } else {
                tickValues = this.chartScale_Measure.ticks(chartAxis_Measure_TickSkip);
            }
        }

        // remove non-integer values & 0...
        tickValues = tickValues.filter(function(d){return d%1===0&&d!==0;});

        var tickDoms = this.DOM.chartAxis_Measure.selectAll("span.tick")
            .data(tickValues,function(i){return i;});
        tickDoms.exit().remove();
        var tickData_new=tickDoms.enter().append("span").attr("class","tick");

        // translate the ticks horizontally on scale
        tickData_new.append("span").attr("class","line");

        // Place the doms at the bottom of the histogram, so their animation is in the right direction
        tickData_new.each(function(){
            kshf.Util.setTransform(this,"translateY("+me.height_hist+"px)");
        });

        if(this.browser.ratioModeActive){
            tickData_new.append("span").attr("class","text").text(function(d){return d;});
        } else {
            tickData_new.append("span").attr("class","text").text(function(d){return d3.format("s")(d);});
        }

        setTimeout(function(){
            var transformFunc;
            if(me.browser.ratioModeActive){
                transformFunc=function(d){
                    kshf.Util.setTransform(this,"translateY("+
                        (me.height_hist-d*me.height_hist/100)+"px)");
                };
            } else {
                if(me.browser.percentModeActive){
                    transformFunc=function(d){
                        kshf.Util.setTransform(this,"translateY("+
                            (me.height_hist-(d/maxValue)*me.height_hist)+"px)");
                    };
                } else {
                    transformFunc=function(d){
                        kshf.Util.setTransform(this,"translateY("+
                            (me.height_hist-me.chartScale_Measure(d))+"px)");
                    };
                }
            }
            var x = me.browser.noAnim;
            if(x===false) me.browser.setNoAnim(true);
            me.DOM.chartAxis_Measure.selectAll(".tick").style("opacity",1).each(transformFunc);
            if(x===false) me.browser.setNoAnim(false);
        });
    },
    /** -- */
    refreshMeasureLabel: function(){
        var me=this;
        if(this.browser.previewedSelectionSummary===this) return;

        this.DOM.aggr_Group.attr("noitems",function(aggr){ return aggr.aggregate_Active===0; });

        this.DOM.measureLabel.each(function(aggr){
            var p=aggr.aggregate_Preview;
            if(me.browser.vizPreviewActive){
                if(me.browser.preview_not)
                    p = aggr.aggregate_Active-aggr.aggregate_Preview;
                else
                    p = aggr.aggregate_Preview;
            } else {
                p = aggr.aggregate_Active;
            }
            if(me.browser.percentModeActive){
                if(me.browser.ratioModeActive){
                    p = 100*p/aggr.aggregate_Active;
                    if(!me.browser.vizPreviewActive){
                        this.textContent = "";
                        return;
                    }
                } else {
                    p = 100*p/me.browser.itemsWanted_Aggregrate_Total;
                }
                if(p<0) p=0;
                this.textContent = p.toFixed(0)+"%";
            } else {
                if(p<0) p=0;
                this.textContent = kshf.Util.formatForItemCount(p);
            }
        });
    },
    /** -- */
    refreshIntervalSlider: function(){
        var minPos = this.valueScale(this.summaryFilter.active.min);
        var maxPos = this.valueScale(this.summaryFilter.active.max);
        // Adjusting min/max position is important because if it is not adjusted, the
        // tips of the filtering range may not appear at the bar limits, which looks distracting.
        if(this.summaryFilter.active.min===this.intervalRange.min){
            minPos = this.valueScale.range()[0];
        }
        if(this.summaryFilter.active.max===this.intervalRange.max){
            maxPos = this.valueScale.range()[1];
        }
        if(this.scaleType==='step'){
            minPos-=this.aggrWidth/2;
            maxPos+=this.aggrWidth/2;
        }

        this.DOM.intervalSlider.select(".base.active")
            .attr("filtered",this.isFiltered())
            .each(function(d){
                kshf.Util.setTransform(this,"translateX("+minPos+"px) scaleX("+(maxPos-minPos)+")");
            });
        this.DOM.intervalSlider.selectAll(".handle")
            .each(function(d){
                kshf.Util.setTransform(this,"translateX("+((d==="min")?minPos:maxPos)+"px)");
            });
    },
    /** -- */
    refreshHeight: function(){
        this.DOM.histogram.style("height",(this.height_hist+this.height_hist_topGap)+"px")
        this.DOM.wrapper.style("height",(this.collapsed?"0":this.getHeight_Wrapper())+"px");
        this.DOM.root.style("max-height",(this.getHeight()+1)+"px");

        var labelTranslate ="translateY("+this.height_hist+"px)";
        if(this.DOM.measureLabel)
            this.DOM.measureLabel.each(function(bar){ kshf.Util.setTransform(this,labelTranslate); });
        if(this.DOM.timeSVG)
            this.DOM.timeSVG.style("height",(this.height_hist+2)+"px");
    },
    /** -- */
    refreshWidth: function(){
        var _width_ = this.getWidth()-this.width_histMargin-this.width_vertAxisLabel;
        this.updateScaleAndBins( _width_, Math.ceil(_width_/this.optimumTickWidth));
        this.updateDOMwidth();
    },
    /** -- */
    setHeight: function(targetHeight){
        if(this.histBins===undefined) return;
        var c = targetHeight-this.getHeight_Header()-this.getHeight_Extra();
        c = Math.min(c,100);
        if(this.height_hist===c) return;
        this.height_hist = c;
        this.updateBarScale2Active();
        this.refreshBins_Translate();

        this.refreshViz_Scale();
        this.refreshViz_Preview();
        this.refreshViz_Compare();
        this.refreshViz_Axis();
        this.refreshHeight();

        this.DOM.labelGroup.style("height",this.height_labels+"px");
        this.DOM.intervalSlider.selectAll(".rangeLimitOnChart")
            .style("height",this.height_hist+"px")
            .style("top",(-this.height_hist-13)+"px")
    },
    /** -- */
    updateAfterFilter: function(resultChange){
        if(this.isEmpty) return;
        this.updateAggregate_Active();
        this.refreshMeasureLabel();
        this.updateBarPreviewScale2Active();
        if(this.showPercentile) this.updatePercentiles();
    },
    /** -- */
    updateBarPreviewScale2Active: function(){
        var me=this;
        this.updateBarScale2Active();
        this.refreshBins_Translate();
        this.refreshViz_Scale();
        this.refreshViz_Compare();

        this.DOM.aggr_Preview.attr("fast",null); // take it slow for result preview animations
        this.refreshViz_Preview();
        this.refreshViz_Axis();

        setTimeout(function(){ me.DOM.aggr_Preview.attr("fast",true); },800);
    },
    /** -- */
    setSelectedPosition: function(v){
        if(!this.inBrowser()) return;
        if(this.DOM.inited===false) return;
        if(v===null) return;
        if(this.valueScale===undefined) return;

        var t="translateX("+(this.valueScale(v))+"px)";
        this.DOM.selectedItemValue
            .each(function(){ kshf.Util.setTransform(this,t); })
            .style("display","block");

        this.DOM.selectedItemValueText.html(
            this.intervalTickFormat(v)+(this.unitName?("<span class='unitName'>"+this.unitName+"</span>"):"")
        );
    },
    /** -- */
    hideSelectedPosition: function(){
        if(this.inBrowser()) this.DOM.selectedItemValue.style("display",null);
    },
    /** -- */
    updatePercentiles: function(){
        var me=this;
        // get active values into an array
        // the items are already sorted by their numeric value, it's just a linear pass.
        var values = [];
        if(!this.hasEntityParent()){
            this.filteredItems.forEach(function(item){
                if(item.isWanted) values.push(me.itemV(item));
            });
        } else {
            this.filteredItems.forEach(function(item){
                if(item.aggregate_Active>0) values.push(me.itemV(item));
            });
        }

        this.quantile_val = {};
        this.quantile_pos = {};
        [10,20,30,40,50,60,70,80,90].forEach(function(q){
            this.quantile_val[q] = d3.quantile(values,q/100);
            this.quantile_pos[q] = this.valueScale(this.quantile_val[q]);
            kshf.Util.setTransform(this.DOM.quantile[q][0][0],"translateX("+this.quantile_pos[q]+"px)");
        },this);

        [[10,90],[20,80],[30,70],[40,60]].forEach(function(qb){
            kshf.Util.setTransform(this.DOM.quantile[""+qb[0]+"_"+qb[1]][0][0],
                "translateX("+(this.quantile_pos[qb[0]])+"px) "+
                "scaleX("+(this.quantile_pos[qb[1]]-this.quantile_pos[qb[0]])+") ");
        },this);
    },
};

for(var index in Summary_Interval_functions){
    kshf.Summary_Interval.prototype[index] = Summary_Interval_functions[index];
}
