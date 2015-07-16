
'use strict';

// Include Gulp & Tools We'll Use
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var merge = require('merge-stream');

function distPath(path) {
  return 'static/dist/' + path;
}

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
