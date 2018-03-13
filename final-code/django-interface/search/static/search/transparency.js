/*
This javascript file uses highcharts demo template online to show the 
histograms of company's transparency score and average transparency scores for all companies. 
The average transparency scores in the charts were hardcoded after computed in pandas. The
transparency scores for each company were inputed from variables defined in html.

Type: 
Modified

Reference:
(1) Highcharts demo
    link: https://www.highcharts.com/demo/column-parsed
*/
Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Brand Transparency Index'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        type: 'category'
    },
    yAxis: [{
        className: 'highcharts-color-0',
        title: {
            text: 'Transparency Scores for Different Dimensions'
        }

    }, {
       className: 'highcharts-color-0',
       opposite: false,
       title: {
            text: 'Average Transparency Scores for Different Dimensions'
        }
    }],

    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}</b> of total<br/>'
    },

    series: [{
        name: 'Brand Transparency Score',
        colorByPoint: false,
        data: [{
            name: 'Policy',
            y: policy,
            drilldown: null
        }, {
            name: 'Tracking',
            y: tracking,
            drilldown: null
        }, {
            name: 'Social',
            y: social,
            drilldown: null
        }, {
            name: 'Engagement',
            y: engage,
            drilldown: null
        }, {
            name: 'Governance',
            y: governance,
            drilldown: null
        }, 
           {
            name: 'Total Score',
            y: score,
            drilldown:null
           }]
    }, 
        {
        name: 'Average Transparency Score',
        data: [{
            name: 'Policy',
            y: 55.4 ,
            drilldown: null
        }, {
            name: 'Tracking',
            y: 24.8,
            drilldown: null
        }, {
            name: 'Social',
            y: 53.2,
            drilldown: null
        }, {
            name: 'Engagement',
            y: 22.8,
            drilldown: null
        }, {
            name: 'Governance',
            y: 44.3,
            drilldown: null
        }, {
            name: 'Total Score',
            y: 42.2,
            drilldown :null

        }]
    }]
    
});