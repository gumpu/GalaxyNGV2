// vi: spell spl=en

var planets = [ {x:10,y:50}, {x:120,y:30}, {x:25,y:200} ];

var i;

for ( i = 0; i < 100; ++i ) {
    planets[ i ] = { x:Math.random()*600, y:Math.random()*600 };
}


MapViewer = function( a_planet_list ) {
    // The number of planets will not change.
    var viewport_size = { width:600, height:300 };
    var canvas_size   = { width:600, height:300 };
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
        draw : function( ctx ) {
            ctx.clearRect(0, 0, canvas_size.width, canvas_size.height);
            for ( var i = 0; i < n; i++ ) {
                a_planet = a_planet_list[ i ];
                console.log( a_planet );
                ctx.fillStyle = "rgba(0, 0, 200, 1.0)";
                ctx.fillRect( a_planet.cx, a_planet.cy, 5, 5 );
            }
        },
        view : function () {
            console.log( a_planet_list );
        } }
}( planets );

console.log( MapViewer );

// MapViewer.view();
// MapViewer.translate( { x:10, y:12 } );
// MapViewer.project();
// MapViewer.view();

