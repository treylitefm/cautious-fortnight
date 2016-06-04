var args = process.argv;

if (args.length <= 2) {
    console.error('Requires host url!');
    process.exit();
}

var matches = args[args.length-1].match(/https?:\/\/[a-z0-9\.]+:?[0-9]{0,5}\//g)

if (matches === null) {
    console.error('Enter your host url! Note: include http[s] and trailing slash. \nExample: http://localhost:1234/ or https://griffin.com/');
    process.exit()
}

var jsonfile = require('jsonfile'),
    manifestPath = './manifest.json',
    configPath = './config.json',
    manifest = require(manifestPath),
    config = {},
    url = matches[0];

config['host_url'] = url;
manifest['permissions'].push(url);
jsonfile.spaces = 4;

jsonfile.writeFile(manifestPath, manifest, function (err) {
      if (err !== null) {
          console.error(err)
      }
});

jsonfile.writeFile(configPath, config, function (err) {
      if (err !== null) {
          console.error(err)
      }
});

console.log('Done!');
