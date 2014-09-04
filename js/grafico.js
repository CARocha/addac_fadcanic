$(function () {
    $('#grafico1').highcharts({
        title: {
            text: 'Grafico combinado'
        },
        xAxis: {
            categories: ['Apples', 'Oranges', 'Pears']
        },
        labels: {
            items: [{
                html: 'Total fruit consumption',
                style: {
                    left: '50px',
                    top: '18px',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                }
            }]
        },
        series: [{
            type: 'column',
            name: 'Jane',
            data: [3, 2, 1]
        }, {
            type: 'column',
            name: 'John',
            data: [2, 3, 5]
        },{
            type: 'spline',
            name: 'Average',
            data: [3, 2.67, 3],
            marker: {
                lineWidth: 2,
                lineColor: Highcharts.getOptions().colors[5],
                fillColor: 'white'
            }
        },]
    });
});
$(function () {
    $('#grafico2').highcharts({
        title: {
            text: 'Grafico combinado'
        },
        xAxis: {
            categories: ['Apples', 'Oranges', 'Pears']
        },
        labels: {
            items: [{
                html: 'Total fruit consumption',
                style: {
                    left: '50px',
                    top: '18px',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                }
            }]
        },
        series: [{
            type: 'column',
            name: 'Jane',
            data: [3, 2, 1]
        }, {
            type: 'column',
            name: 'John',
            data: [2, 3, 5]
        },{
            type: 'spline',
            name: 'Average',
            data: [3, 2.67, 3],
            marker: {
                lineWidth: 2,
                lineColor: Highcharts.getOptions().colors[7],
                fillColor: 'white'
            }
        },]
    });
});