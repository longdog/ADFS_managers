import 'bootstrap/dist/js/bootstrap';
import 'antd/dist/antd.css';

import { renderSurvey } from './survey';
import { renderStadionForm } from './stadionReservation';
import { renderLoginForm } from './login';
import store from './store';

var $ = require('jquery');
window.jQuery = $;
window.$ = $;
window.store = store;

$(document).ready(function(){
  const $loginForm = $('#login-form');
  if (window.location.pathname === '/survey') renderSurvey();
  if (window.location.pathname === '/logic/stadion/get/') renderStadionForm();
  renderLoginForm();
});
