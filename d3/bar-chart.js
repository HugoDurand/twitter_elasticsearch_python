// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom,
    dataList = []
    i = 0;

let colors = [ "#6d3580", "#cc4165", "#e4734f", "#00a8b5" ];

// set the ranges
var x = d3.scaleBand()
          .range([0, width])
          .padding(0.1);
var y = d3.scaleLinear()
          .range([height, 0]);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("class", "bar-chart")
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

d3.csv("./csv/occurence_festival.csv", function(error, data) {
  Object.entries(data[0]).forEach(entry => {
    let el = {
      festival: entry[0],
      occurrence: parseInt(entry[1]),
      color: colors[i]
    };
    console.log(parseInt(entry[1]));
    dataList.push(el);
    i++;
  });

  console.log(dataList)

  if (error) throw error;

  x.domain(dataList.map(function(d) { return d.festival; }));
  y.domain([0, d3.max(dataList, function(d) { return d.occurrence; })]);

  svg.selectAll(".bar")
      .data(dataList)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.festival); })
      .attr("width", x.bandwidth())
      .attr("y", function(d) { return y(d.occurrence); })
      .attr("height", function(d) { return height - y(d.occurrence); })
      .attr("fill", function(d){ return d.color });

  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .attr("class", "axisx")
      .call(d3.axisBottom(x));

  svg.append("g")
      .attr("class", "axisy")
      .call(d3.axisLeft(y));

  svg.selectAll(".text")
      .data(dataList)
      .enter().append('text')
      .attr("class","label")
      .attr("dy", ".75em")
      .attr('x', function(d) { return x(d.festival); })
      .attr('y', function(d) { return y(d.occurrence + 30); })
      .attr("transform", "translate(90,0)")
      .text(function(d) { return Math.round(d.occurrence); });
});
