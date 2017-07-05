////////////////////////////////
//Setup//
////////////////////////////////

// Plugins
var gulp = require('gulp'),
  pjson = require('./package.json'),
  gutil = require('gulp-util'),
  sass = require('gulp-sass'),
  autoprefixer = require('gulp-autoprefixer'),
  cssnano = require('gulp-cssnano'),
  rename = require('gulp-rename'),
  del = require('del'),
  plumber = require('gulp-plumber'),
  pixrem = require('gulp-pixrem'),
  uglify = require('gulp-uglify'),
  imagemin = require('gulp-imagemin'),
  spawn = require('child_process').spawn,
  runSequence = require('run-sequence'),
  browserSync = require('browser-sync').create(),
  reload = browserSync.reload;


// Relative paths function
var pathsConfig = function (appName) {
  this.app = './' + (appName || pjson.name);

  return {
    app: this.app,
    css: this.app + '/static/css',
    sass: this.app + '/static/sass',
    fonts: this.app + '/static/fonts',
    images: this.app + '/static/images',
    js: this.app + '/static/js',
  }
};

var paths = pathsConfig();

////////////////////////////////
//Tasks//
////////////////////////////////

// Styles autoprefixing and minification
gulp.task('styles', function() {
  return gulp.src([paths.sass + '/main.sass', paths.sass + '/below_the_fold.sass'])
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(autoprefixer({browsers: ['last 2 versions']})) // Adds vendor prefixes
    .pipe(pixrem())  // add fallbacks for rem units
    .pipe(gulp.dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(cssnano()) // Minifies the result
    .pipe(gulp.dest(paths.css))
    .pipe(browserSync.stream());
});

// Javascript minification
gulp.task('scripts', function() {
  return gulp.src(paths.js + '/project.js')
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest(paths.js));
});

// Image compression
gulp.task('imgCompression', function(){
  return gulp.src(paths.images + '/*')
    .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
    .pipe(gulp.dest(paths.images))
});

// Run django server
gulp.task('runServer', function(cb) {
  var cmd = spawn('python', ['manage.py', 'runserver'], {stdio: 'inherit'});
  cmd.on('close', function(code) {
    console.log('runServer exited with code ' + code);
    cb(code);
  });
});

// Browser sync server for live reload
gulp.task('browserSync', function() {
  browserSync.init({
    proxy: 'localhost:8000'
  });
  gulp.watch(paths.sass + '/*.sass', ['styles']);
  gulp.watch(paths.html + '/*.html').on('change', browserSync.reload);
});

// Watch
gulp.task('watch', function() {
  runSequence(['styles', 'scripts', 'imgCompression']);
  gulp.watch(paths.sass + '/*.sass', ['styles']);
  gulp.watch(paths.js + '/*.js', ['scripts']).on('change', reload);
  gulp.watch(paths.images + '/*', ['imgCompression']);
});

// Default task
gulp.task('default', function() {
  runSequence(['styles', 'scripts', 'imgCompression'], 'runServer', 'browserSync', 'watch');
});
