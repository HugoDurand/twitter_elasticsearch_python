// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom,
    dataList = []
    i = 0;

let colors = [ "#11144c", "#3a9679", "#fabc60", "#dd6b4d" ,"#e16262" ];

// set the ranges
var x = d3.scaleBand()
          .range([0, width])
          .padding(0.1);
var y = d3.scaleLinear()
          .range([height, 0]);

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

d3.csv("output.csv", function(error, data) {
  Object.entries(data[0]).forEach(entry => {
    let el = {
      festival: entry[0],
      occurrence: parseInt(entry[1]),
      color: colors[i]
    };
    dataList.push(el);
    i++;
  });

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
      .attr('y', function(d) { return y(d.occurrence + 15); })
      .attr("transform", "translate(67,0)")
      .text(function(d) { return Math.round(y(d.occurrence)); });

      // .attr("x", (function(d) { return xScale(d.food) + xScale.rangeBand() / 2 ; }  ))
      // .attr("y", function(d) { return yScale(d.quantity) + 1; })
      // .attr("dy", ".75em")
      // .text(function(d) { return d.quantity; });

      // .attr('x', function(d) { return x(d.festival); })
      // .attr('y', function(d) { return y(d.occurrence); })
      // .attr("height", function(d) { return height - y(d.occurrence); })
      // .attr('text-anchor', 'middle')
      // .text(function(d) { return y(d.occurrence); });



  // svg.selectAll(".text")
  //     .data(dataList)
  //     .enter().append('text')
  //     .attr('x', -(height / 2) - margin)
  //     .attr('y', margin / 2.4)
  //     .attr('transform", "translate(0," + height + ")')
  //     .attr('text-anchor', 'middle')
  //     .text('Love meter (%)')

});
