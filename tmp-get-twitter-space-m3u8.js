HOW_MANY_TIMES_YOU_WANT_TO_READ_NETWORK_TRAFFIC = 8

strPlaylistm3u8 = '';
maxCount = HOW_MANY_TIMES_YOU_WANT_TO_READ_NETWORK_TRAFFIC;
displayDelay = maxCount+1000;
for(var count=0; count<10; count++){
    delayInMs = count * 1000;
    setTimeout( ()=>{
        aryEntries = window.performance.getEntries();
        for(var i=0; i<aryEntries.length; i++){
            if( aryEntries[i].name.indexOf("audio-space")>0 && 
                aryEntries[i].name.indexOf("playlist")>0 && 
                aryEntries[i].name.indexOf("m3u8")>0 ){
                //playlist m3u8 found!
                strPlaylistm3u8 = aryEntries[i].name;
                break;
            }
        }
    }, delayInMs );
}
document.querySelector("[aria-label='Play recording']").click()

setTimeout( ()=>{
    console.log('strPlaylistm3u8')
    console.log(strPlaylistm3u8)
}, displayDelay )

