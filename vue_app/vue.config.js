const BundleTracker = require("webpack-bundle-tracker");
const path = require('path');

module.exports = {
  publicPath: "http://localhost:8080/",
  outputDir: path.resolve(__dirname, './dist/'),

  chainWebpack: config => {

    config.optimization.splitChunks(false);

    config.plugin('BundleTracker')
      .use(BundleTracker, [{path: path.resolve(__dirname, './dist/'), filename: 'webpack-stats.json'}]);

    config.resolve.alias
      .set('__STATIC__', 'static');

    config.devServer
      //.public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .https(false)
      .headers({"Access-Control-Allow-Origin": ["*"]});
  }
};
