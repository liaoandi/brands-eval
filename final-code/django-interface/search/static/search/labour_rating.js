/*
This javascript file uses highcharts demo template online to show the 
stacked histogram of company's labour ratings. The figures in the charts were
hardcoded after computed in pandas.

Type: 
Modified

Reference:
(1) Highcharts demo
    link: https://www.highcharts.com/demo/column-stacked
*/
Highcharts.chart(context_var, {
    height:50, 
    
    chart: {
        type: 'column'
    },
    title: {
        text: 'Labour Rating Classification Chart'
    },
    xAxis: {
        categories: ['A', 'B', 'C', 'D', 'F']
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Classification in Each Grade'
        },
        stackLabels: {
            enabled: false,
            style: {
                fontWeight: 'bold',
                color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
            }
        }
    },
    legend: {
        align: 'right',
        x: 0,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: false,
                color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
            }
        }
    },
    series: [{
        name: '+',
        data: [{
        name:"A+",
        y: 3},
        {
        name:"B+", 
        y: 40}, 
        {name:"C+",
        y: 62}, 
        {name:"D+",
        y:21}]
    }, {
        name: '',
        data: 
        [{
        name:"A",
        y: 8},
        {
        name:"B", 
        y: 24}, 
        {name:"C",
        y: 41}, 
        {name:"D",
        y: 4},
        {name: "F",
        y: 35}]
    }, {
        name: '-',
        data: 
        [{
        name:"A-",
        y: 6},
        {
        name:"B-", 
        y: 49}, 
        {name:"C-",
        y: 8}, 
        {name:"D-",
        y: 4}]
    },
    {
        type: 'pie',
        name: 'Total Labour Rating Classification',
        data: [{
            name: 'A',    
            y: 17,
            color: Highcharts.getOptions().colors[0] // 
        }, {
            name: 'B',
            y: 113,
            color: Highcharts.getOptions().colors[1] // 
        }, {
            name: 'C',
            y: 111,
            color: Highcharts.getOptions().colors[2] // 
        }, {
            name: 'D',
            y: 29,
            color: Highcharts.getOptions().colors[3] // 
        }, {
            name: 'F',
            y: 35,
            color: Highcharts.getOptions().colors[4] // 
        }],
        center: [60, 80],
        size: 45,
        showInLegend: false,
        dataLabels: {
            enabled: true,
            borderRadius: 3
        }
    }
    ]
});