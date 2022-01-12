"use strict"; //Set environment variable (Used for development and demo)

/* 
    Possible values:
    1. development
    2. customization
*/

var env = 'development';
initPageloader();
$(document).ready(function () {
  if (env === 'development') {
    changeDemoImages();
  }

  initNavbarBurger();
  initFullscreenSlider();
  initShopSidebar();
  initProductDetailsLinks();
  initOrderDetailsLinks();
  initCartSidebar();
  initGlobalSearch();
  initFilterSidebar();
  initCategoriesSidebar();
  feather.replace();
  initTabs();
  initDropdowns();
  initModals();
  initClosableMessage();
  initChosenSelects();
  initBackgroundImages();
  initFileInputs(); //Check viewport size

  if (!mobileTrue) {
    initPopovers();
  }

  initCardActions();
  initAnimatedCheckboxes();
  initMobileMode();
  getCart();
});