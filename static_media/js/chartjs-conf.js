var Script = function () {


    var doughnutData = [
        {
            value: 30,
            color:"#1abc9c",
            label: "label1",
            title: 'label1'
        },
        {
            value : 50,
            color : "#2ecc71",
            label: "label2",
            title: 'label2'
        },
        {
            value : 100,
            color : "#3498db",
            label: "label3",
            title: 'label3'
        },
        {
            value : 40,
            color : "#9b59b6",
            label: "label4",
            title: 'label4'
        },
        {
            value : 120,
            color : "#34495e",
            label: "label5",
            title: 'label5'
        }

    ];
        var doughnutData2 = [
        {
            value: 30,
            color:"#1abc9c",
            label: "label1",
            title: 'label1'
        },
        {
            value : 50,
            color : "#2ecc71",
            label: "label2",
            title: 'label2'
        },
        {
            value : 100,
            color : "#3498db",
            label: "label3",
            title: 'label3'
        },
        {
            value : 40,
            color : "#9b59b6",
            label: "label4",
            title: 'label4'
        },
        {
            value : 120,
            color : "#34495e",
            label: "label5",
            title: 'label5'
        }

    ];

    var pieData = [
        {
            value: 30,
            color:"#1abc9c",
            label: "label1",
            title: 'label1'
        },
        {
            value : 50,
            color : "#16a085",
            label: "label2",
            title: 'label2'
        },
        {
            value : 100,
            color : "#27ae60",
            label: "label3",
            title: 'label3'
        }

    ];
        var pieData2 = [
        {
            value: 30,
            color:"#1abc9c",
            label: "label1",
            title: 'label1'
        },
        {
            value : 50,
            color : "#16a085",
            label: "label2",
            title: 'label2'
        },
        {
            value : 100,
            color : "#27ae60",
            label: "label3",
            title: 'label3'
        }

    ];
    var barChartData = {
        labels : ["2009","2011","2013"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                data : [65,59,90],
                title: 'label1'
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,1)",
                data : [28,48,40],
                title: 'label2'
            }
        ]

    };
       var barChartData2 = {
        labels : ["2009","2011","2013"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                data : [65,59,90],
                title: 'label1'
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,1)",
                data : [2,8,40],
                title: 'label2'
            }
        ]

    };


    Chart.defaults.global.responsive = true;
    Chart.defaults.global.scaleShowLabels =  true;
    new Chart(document.getElementById("doughnut").getContext("2d")).Doughnut(doughnutData);
    legend(document.getElementById("doughnutLegend"), doughnutData);
    new Chart(document.getElementById("doughnut2").getContext("2d")).Doughnut(doughnutData2);
    legend(document.getElementById("doughnutLegend2"), doughnutData2);
    new Chart(document.getElementById("bar").getContext("2d")).Bar(barChartData);
    legend(document.getElementById("barLegend"), barChartData);
    new Chart(document.getElementById("bar2").getContext("2d")).Bar(barChartData2);
    legend(document.getElementById("barLegend2"), barChartData2);
    new Chart(document.getElementById("pie").getContext("2d")).Pie(pieData);
    legend(document.getElementById("pieLegend"), pieData);
    new Chart(document.getElementById("pie2").getContext("2d")).Pie(pieData2);
    legend(document.getElementById("pieLegend2"), pieData2);


}();