var bodyText=[ "The smaller your reality, the more convinced you are that you know everything.", "If the facts don't fit the theory, change the facts.", "The past has no power over the present moment.", "This, too, will pass.", "</p><p>You will not be punished for your anger, you will be punished by your anger.", "Peace comes from within. Do not seek it without.", "<h3>Heading</h3><p>The most important moment of your life is now. The most important person in your life is the one you are with now, and the most important activity in your life is the one you are involved with now." ]
function generateText( sentenceCount ) {
    for ( var i=0; i<sentenceCount; i++ )
    {
        document.write( bodyText[ Math.floor( Math.random()*7 ) ] + " " );
    }
}

// 1) Send get request to Flask server, and get the OHLC data json object
// 2) Update Google Chart periodically in a configurable interval setting from the frontend
// 3) Implement buy and sells and profit tracking from the frontend

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
    ['Mon', 20, 28, 38, 45],
    ['Tue', 31, 38, 55, 66],
    ['Wed', 50, 55, 77, 80],
    ['Thu', 77, 77, 66, 50],
    ['Fri', 68, 66, 22, 15]
    // Treat first row as data as well.
    ], true);

    var options = {
    legend:'none'
    };

    var chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}