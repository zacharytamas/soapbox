
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

  var vulcanized = gulp.src([distPath('elements/components-core.html')])
    .pipe($.rename('components-core.vulcanized.html'))
    .pipe(gulp.dest('static/dist/components'));

  return merge(bower, elements, vulcanized)
    .pipe($.size({title: 'copy'}));

});
