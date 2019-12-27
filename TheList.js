// var $  = require( 'jquery' );
// var dt = require( 'datatables.net' )();

$(document).ready( function () {
    d3.text("TheList.csv", function(data) {
        var parsedCSV = d3.csv.parseRows(data);

        var table = d3.select("table_id")
            .selectAll("tr")
                .data(parsedCSV).enter()
                .append("tr")

            .selectAll("td")
                .data(function(d) { return d; }).enter()
                .append("td")
                .text(function(d) { return d; });
    });
    $('#table_id').DataTable();
} );
