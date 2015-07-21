
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var browserSync = require('browser-sync');
var merge = require('merge-stream');
var path = require('path');

function distPath(path) {
  return 'static/dist/' + path;
}

var styleTask = function(stylesPath, srcs) {
  return gulp
    .src(srcs.map(function(src) {
      return path.join('static', stylesPath, src); }
    ))
    // .pipe($.changed('static/' + stylesPath, {extension: '.css'}))
    // TODO possibly add CSS minification here
    .pipe(gulp.dest('static/dist/' + stylesPath))
    .pipe($.size({title: stylesPath}));
};

gulp.task('styles', styleTask.bind(gulp, '', ['*.css']));

gulp.task('copy', function() {
  var bower = gulp.src([
    'bower_components/**/*'
  ]).pipe(gulp.dest(distPath('bower_components')));

  var elements = gulp.src(['static/elements/**/*.html'])
    .pipe(gulp.dest(distPath('elements')));

  var vulcanized = gulp.src([distPath('elements/core.html')])
    .pipe($.rename('core.vulcanized.html'))
    .pipe(gulp.dest(distPath('elements')));

  return merge(bower, elements, vulcanized)
    .pipe($.size({title: 'copy'}));
});

// Vulcanize imports
gulp.task('vulcanize', function() {
  var DEST_DIR = 'static/dist/elements';

  return gulp.src('static/dist/elements/core.vulcanized.html')
    .pipe($.vulcanize({
      stripComments: true,
      inlineCss: true,
      inlineScripts: true
    }))
    .pipe(gulp.dest(DEST_DIR))
    .pipe($.size({title: 'vulcanize'}));
});

gulp.task('develop', function() {

  browserSync({
    notify: false,
    logPrefix: 'PSK',
    snippetOptions: {
      rule: {
        match: '<span id="browser-sync-binding"></span>',
        fn: function(snippet) {
          return snippet;
        }
      }
    },
    proxy: 'localhost:8080'
  });

  gulp.watch(['static/*.css'], ['styles']);
  gulp.watch(['static/dist/*.css'], browserSync.reload);
});
