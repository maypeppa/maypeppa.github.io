/*******************************
 * usage: phantomjs get.js url
 *******************************/

var system = require('system');
var page = require('webpage').create();  

page.settings.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.3 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.3'
page.settings.resourceTimeout = 30000 // 30s, in milli-secs


args = system.args;

if (args.length !== 2) {
    phantom.exit();
}

url = args[1];

page.open(url, function (status) {
    if (status === 'success') {
        var p = page.evaluate(function () {
            return document.documentElement.outerHTML;
        });
        console.log(p);
    }
    phantom.exit();
});
