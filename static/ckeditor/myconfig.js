// ckeditor의 config를 위한 주석

CKEDITOR.editorConfig = function (config) {
  config.extraPlugins = "uploadfile,uploadimage";
  config.filebrowserUploadUrl = "/media/upload/";
  config.fillEmptyBlocks = false;
};
