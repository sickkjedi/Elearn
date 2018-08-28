const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: {
    'student/anton': './student/static/student/js/main.js'
  },
  output: {
    path: path.resolve(__dirname, './static/dist/js/'),
    publicPath: '/static/dist/js/',
    filename: '[name].bundle.min.js'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          // Other vue-loader options go here.
          loaders: {}
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      {
        // Force webpack to load modules using only CommonJS (disable AMD support).
        // Doesn't touch the require define functions.
        test: /\.js$/,
        use: 'imports-loader?define=>false'
      },
      {
        // Make sure all bootstrap/js files get jQuery loaded when required.
        // Using imports-loader to attach require.
        test: /bootstrap\/js\/(.+?)\.js$/,
        use: 'imports-loader?jQuery=jquery'
      },
      {
        test: /\.(eot|woff|woff2|ttf|svg|png|jpe?g|gif)(\?\S*)?$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  plugins: [],
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  // NOTE: This is to prevent bundling some assets we already have on the page, therefore having multiple copies and introducing
  // overhead and/or potential clashes. We just let outside wrapper do this work for us.
  // In our cases that's require.js so we use predefined configure-require paths.
  externals: {
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
};

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map';
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
