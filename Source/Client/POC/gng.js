/* vi: spell spl=en 
 */

// Assumes jQuery
//
$( document ).ready(function() {
    console.log( 'ready!' );

    //var canvas = document.getElementById('map');
    var canvas = $('canvas#map');
    if (canvas[0].getContext){
        var ctx = canvas[0].getContext('2d');
        // drawing code here
        console.log( 'ready to draw!' );

        MapViewer.translate( { x:0, y:0 } );
        MapViewer.project( );
        MapViewer.draw( ctx );
        MapViewer.view();
    } else {
        // canvas-unsupported code here
        console.log( 'Where is the canvas!' );
    }

    //  var canvas = $('#my_canvas');

    // calculate position of the canvas DOM element on the page
    var canvasPosition = {
        x: canvas.offset().left,
        y: canvas.offset().top
    };
    console.log( canvasPosition );

    if ( false ) {
    canvas.mousemove( function(e) {
        // use pageX and pageY to get the mouse position
        // relative to the browser window
        var mouse = {
            x: e.pageX - canvasPosition.x,
            y: e.pageY - canvasPosition.y
        }
        console.log( 'click' + mouse.x + ',' + mouse.y );
        // now you have local coordinates,
        // which consider a (0,0) origin at the
        // top-left of canvas element
    });
    }

    if ( false ) {
    $.getJSON("dummy.json", function(data) {
        console.log(data);
        //console.log(data.planets.p488);
        // data is a JavaScript object now. Handle it as such
    });
    }
});

