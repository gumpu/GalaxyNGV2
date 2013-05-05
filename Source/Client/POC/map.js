// vi: spell spl=en

// Viewport
//

var translate = { dx:0, dy:0 };
var scale     = { s:1 };

var planets = [ {x:10,y:20}, {x:12,y:3}, {x:25,y:30} ];

MapViewer = function( a_planet_list ) {
    // The number of planets will not change.
    var viewport_size = { width:100, height:50 };
    var canvas_size   = { width:50,  height:25 };
    var n = a_planet_list.length;
    return {
        translate : function ( translation ) {
            for ( var i = 0; i < n; i++ ) {
                a_planet = a_planet_list[ i ];
                a_planet.vx = a_planet.x - translation.x;
                a_planet.vy = a_planet.y - translation.y;
            }
        },
        project : function( ) {
            scale = canvas_size.width / viewport_size.width;
            for ( var i = 0; i < n; i++ ) {
                a_planet = a_planet_list[ i ];
                a_planet.cx = a_planet.vx * scale;
                a_planet.cy = (canvas_size.height - a_planet.vy) * scale;
            }
        },
        view : function () {
            console.log( a_planet_list );
        } }
}( planets );

//console.log( MapViewer );

MapViewer.view();
MapViewer.translate( { x:10, y:12 } );
MapViewer.project();
MapViewer.view();

