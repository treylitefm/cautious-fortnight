function getCurrentTabUrl(callback) {
    var queryInfo = {
        active: true,
        currentWindow: true
    }

    chrome.tabs.query(queryInfo, function(tabs) {
        var tab = tabs[0]

        var url = tab.url;
        console.assert(typeof url == 'string', 'tab.url should be a string');

        callback(url)
    });
}

function renderText(text) {
    document.getElementById('status').textContent = renderText;
}

function getUrl() {
    return config['host_url'];
}

document.addEventListener('DOMContentLoaded', function() {
    getCurrentTabUrl(function(url) {
        console.log('oamrrrr', url);
        var xhttp = new XMLHttpRequest(),
            url = getUrl();
        xhttp.open("POST", url+"download", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify({
            url:url
        }));
    });
});
