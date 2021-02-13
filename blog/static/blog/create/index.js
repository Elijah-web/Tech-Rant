const editor = new EditorJS({
    holder: 'editorjs',
/** 
     * Available Tools list. 
     * Pass Tool's class or Settings object for each Tool you want to use 
     */
   tools:{
      raw:RawTool,
       header:Header,
       delimiter: Delimiter,
       paragraph: {
        class: Paragraph,
        inlineToolbar: true,
      },
      embed: Embed,
      image: SimpleImage,
   }
}
);
function myFunction(){
  editor.save().then((output)=>{
    console.log('Data: ',output);
    var json_me = JSON.stringify(output)
    //document.getElementById("demo").innerHTML = json_me;
    // send the string to the server\
    var content = document.getElementById("content");
    content.value = json_me;
    return true;
  }).catch((error)=>{
  console.log('Saving failed:',error)
  });
}