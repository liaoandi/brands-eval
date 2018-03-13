
/*
This javascript file uses highcharts demo template online to show the 
radar plot of our data size in each dimension. The figures in the charts were
hardcoded after computed in pandas.

Type: 
Modified

Reference:
(1) Highcharts demo
    link: https://www.highcharts.com/demo/polar-spider
*/
Highcharts.chart('dimension', {

    chart: {
        polar: true,
        type: 'line'
    },

    title: {
        text: 'Known Data Size by Dimension',
        x: -30
    },

    pane: {
        size: '80%',
    },

    xAxis: {
        categories: ['Transparency', 'Labour', 'Wage', 'Animal', 'Business Ethics', 'Environment', 'Social', 'Other Information'],
        tickmarkPlacement: 'on',
        lineWidth: 0, 
    },

    yAxis: {
        gridLineInterpolation: 'octagon',
        lineWidth: 0,
        min: 0
    },

    tooltip: {
        shared: true,
        pointFormat: '<span style="color:{series.color}">{series.name}: <b>{point.y:,.0f}</b><br/>'
    },

    legend: {
        align: 'right',
        verticalAlign: 'top',
        y: 100,
        x: -10,
        layout: 'vertical'
    },

    series: [{
        name: 'Data Size',
        data: [20, 191, 42, 113, 379, 180, 581, 65],
        pointPlacement: 'on'
    }]

});