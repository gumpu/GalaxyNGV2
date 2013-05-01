/* vi: spell spl=en 
 */

// Assumes jQuery
//
$( document ).ready(function() {
    console.log( 'ready!' );

    // var canvas = document.getElementById('map');
    var canvas = $('#map');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
        // drawing code here
        console.log( 'ready to draw!' );
        ctx.fillStyle = "rgb(200,0,0)";
        ctx.fillRect (10, 10, 55, 50);
     
        ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
        ctx.fillRect (30, 30, 55, 50);
    } else {
          // canvas-unsupported code here
    }

    //  var canvas = $('#my_canvas');

    // calculate position of the canvas DOM element on the page
    var canvasPosition = {
        x: canvas.offset().left,
        y: canvas.offset().top
    };

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

    $.getJSON("dummy.json", function(data) {
        console.log(data);
        console.log(data.planets.p488);

        // data is a JavaScript object now. Handle it as such

    });
});

