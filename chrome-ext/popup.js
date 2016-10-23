var hostUrl;

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
    document.getElementById('notif').textContent = text;
}

function renderTextOnSuccess(xhr) {
    if (xhr['status'] == 200) {
        renderText(':)');
    } else {
        renderText('Ruh-Roh');
    }
}

function loadDoc(url, callback, args) {
    var xhr = new XMLHttpRequest(),
        args = args ? args : {},
        method = args['method'] ? args['method'] : "GET",
        postData = args['postData'] ? args['postData'] : undefined,
        headers = args['headers'] ? args['headers'] : {};

    
    xhr['onreadystatechange'] = function() {
        if (xhr['readyState'] == 4) {
            if (xhr['status'] == 200){
                if (callback) {
                    callback(xhr);
                }
            } else {
                renderText('Ruh-Roh!'); 
            }
        }    
    }

    xhr.open(method, url, true);
    
    for (i in headers) {
        xhr.setRequestHeader(i, headers[i]);
    }

    if (method === "POST" && postData) {
        xhr.send(JSON.stringify(postData));
    } else {
        xhr.send();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    getCurrentTabUrl(function(url) {

        var loadConfig = function() {
            // Load config, set host url, then post url to server

            var postUrl = function() {
                loadDoc(hostUrl+"download", renderTextOnSuccess, {
                    "method": "POST",
                    "postData": {"url": url},
                    "headers": {"Content-Type": "application/json;charset=UTF-8"}
                });
            }

            var setHostUrl = function(xhr) {
                hostUrl = JSON.parse(xhr['response'])['host_url'];
                postUrl();
            }

             loadDoc(chrome.extension.getURL('/config.json'), setHostUrl);
        }

        loadConfig()


    });
});
