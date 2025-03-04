function solution(m, musicinfos) {
    m = parseMusic(m);
    let answer = null;
    
    for (let info of musicinfos) {;
        let [start, end, title, melody] = info.split(',');
        const playtime = getTime(start, end);
        melody = parseMusic(melody);
        
        let totalMelody = '';
        let melodyLen = melody.length;
        totalMelody = melody.repeat(Math.floor(playtime / melodyLen)) +
                        melody.slice(0, playtime % melodyLen);
        
        if (totalMelody.includes(m)) {
            if (!answer || playtime > answer.playtime) {
                answer = { title, playtime }
            }
        }
    }
    
    return answer ? answer.title : '(None)';

}

function parseMusic(music) {
    return music.replace(/C#/g, 'c')
                .replace(/D#/g, 'd')
                .replace(/F#/g, 'f')
                .replace(/G#/g, 'g')
                .replace(/A#/g, 'a')
                .replace(/B#/g, 'b');
}

function getTime(s, e) {
        let start = s.split(':').map(Number);
        let end = e.split(':').map(Number);
        
        start = start[0] * 60 + start[1];
        end = end[0] * 60 + end[1];
        
        return end - start;
}
