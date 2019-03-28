// const d3 =require('d3v4');

// set the dimensions and margins of the graph
// var margin = {top: 20, right: 20, bottom: 30, left: 40},
// width = 960 - margin.left - margin.right,
// height = 500 - margin.top - margin.bottom,
// listKey = [],
// listValue= [],
// listData = [];

// // set the ranges
// var x = d3.scaleBand()
//           .range([0, width])
//           .padding(0.1);

// var y = d3.scaleLinear()
//           .range([height, 0]);

// // append the svg object to the body of the page
// // append a 'group' element to 'svg'
// // moves the 'group' element to the top left margin
// var svg = d3.select("body").append("svg")
//           .attr("width", width + margin.left + margin.right)
//           .attr("height", height + margin.top + margin.bottom)
//           .append("g")
//           .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// // get the data
// d3.csv("output.csv", (error, data) => {

//   data = data[0];
//   console.log("data =>", data)

//   Object.keys(data).map((objectKey, index) => {
//     listKey.push(objectKey);
//     value = data[objectKey];
//     listValue.push(value);
//   });
//   listKey.unshift('Festivals');
//   listValue.unshift('Itération');
//   listData.push(listKey, listValue);
//   console.log("listData =>", listData);


  var svgWidth = 500;
  var svgHeight = 300;

  var svg = d3.select('svg')
      .attr("width", svgWidth)
      .attr("height", svgHeight)
      .attr("class", "bar-chart");

  var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];

  var barPadding = 5;
  var barWidth = (svgWidth / dataset.length);

  var barChart = svg.selectAll("rect")
      .data(dataset)
      .enter()
      .append("rect")
      .attr("y", function(d) {
          return svgHeight - d
      })
      .attr("height", function(d) {
          return d;
      })
      .attr("width", barWidth - barPadding)
      .attr("transform", function (d, i) {
          var translate = [barWidth * i, 0];
          return "translate("+ translate +")";
      });

  // listData.forEach(function(d) {
  //   d.date = parseDate(d.date);
  //   d.value = +d.value;
  // });

  // x.domain(data.map(function(d) { return d.date; }));
  // y.domain([0, d3.max(data, function(d) { return d.value; })]);

  // if (error) throw error;

  // // format the data
  // data.forEach((d) => {
  //   d.sales = +d.sales;
  // });

  // // Scale the range of the data in the domains
  // x.domain(data.map((d) => { return d.salesperson; }));
  // y.domain([0, d3.max(data, (d) => { return d.sales; })]);

  // // append the rectangles for the bar chart
  // svg.selectAll(".bar")
  //     .data(data)
  //     .enter().append("rect")
  //     .attr("class", "bar")
  //     .attr("x", (d) => { return x(d.salesperson); })
  //     .attr("width", x.bandwidth())
  //     .attr("y", (d) => { return y(d.sales); })
  //     .attr("height", (d) => { return height - y(d.sales); });

  // // add the x Axis
  // svg.append("g")
  //     .attr("transform", "translate(0," + height + ")")
  //     .call(d3.axisBottom(x));

  // // add the y Axis
  // svg.append("g")
  //     .call(d3.axisLeft(y));

// });