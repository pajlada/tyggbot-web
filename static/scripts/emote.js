var bttv_cdn = 'https://cdn.betterttv.net/emote/';
var twitch_cdn = 'https://static-cdn.jtvnw.net/emoticons/v1/';
var emotes = {
    /* Twitch Emotes */
    '4Head': { src: twitch_cdn + '354/1.0', },
    'BabyRage': { src: twitch_cdn + '22639/1.0', },
    'BibleThump': { src: twitch_cdn + '86/1.0', },
    'BrokeBack': { src: twitch_cdn + '4057/1.0', },
    'CougarHunt': { src: twitch_cdn + '21/1.0', },
    'DatSheffy': { src: twitch_cdn + '170/1.0', },
    'DansGame': { src: twitch_cdn + '33/1.0', },
    'EleGiggle': { src: twitch_cdn + '4339/1.0', },
    'FailFish': { src: twitch_cdn + '360/1.0', },
    'HeyGuys': { src: twitch_cdn + '30259/1.0', },
    'Kappa': { src: twitch_cdn + '25/1.0', },
    'KappaPride': { src: twitch_cdn + '55338/1.0', },
    'Keepo': { src: twitch_cdn + '1902/1.0', },
    'Kreygasm': { src: twitch_cdn + '41/1.0', },
    'OMGScoots': { src: twitch_cdn + '91/1.0', },
    'OpieOP': { src: twitch_cdn + '356/1.0', },
    'panicBasket': { src: twitch_cdn + '22998/1.0', },
    'PogChamp': { src: twitch_cdn + '88/1.0', },
    'ResidentSleeper': { src: twitch_cdn + '245/1.0', },
    'SMOrc': { src: twitch_cdn + '52/1.0', },
    'SwiftRage': { src: twitch_cdn + '34/1.0', },   
    'TriHard': { src: twitch_cdn + '171/1.0', },
    'VaultBoy': { src: twitch_cdn + '54090/1.0', },
    'WutFace': { src: twitch_cdn + '28087/1.0', },
    '<3': { src: twitch_cdn + '9/1.0', },
    /* Tyggbar Emotes */
    'aiaW': { src: twitch_cdn + '38579/1.0', },
    'aiaKappa': { src: twitch_cdn + '39089/1.0', },
    'aiaMom': { src: twitch_cdn + '41294/1.0', },
    'aiaKiss': { src: twitch_cdn + '48298/1.0', },
    'aiaFail': { src: twitch_cdn + '48069/1.0', },
    'aiaEars': { src: twitch_cdn + '48825/1.0', },
    'aiaOk': { src: twitch_cdn + '56519/1.0', },
    'aiaL': { src: twitch_cdn + '56518/1.0', },
    /* Forsen Emotes */ 
    'forsenKev': { src: twitch_cdn + '24548/1.0', },
    'forsenSambool': { src: twitch_cdn + '45561/1.0', },
    'forsenSnus': { src: twitch_cdn + '12893/1.0', },
    'forsenGasm': { src: twitch_cdn + '13074/1.0', },
    'forsenODO': { src: twitch_cdn + '17303/1.0', },
    'forsenWOW': { src: twitch_cdn + '19927/1.0', },
    'forsenOP': { src: twitch_cdn + '27611/1.0', },
    'forsenPlugdj': { src: twitch_cdn + '29192/1.0', },
    'forsenRP': { src: twitch_cdn + '31100/1.0', },
    'forsenW': { src: twitch_cdn + '31021/1.0', },
    'forsenSwag': { src: twitch_cdn + '31014/1.0', },
    'forsen30': { src: twitch_cdn + '31186/1.0', },
    'forsenBoys': { src: twitch_cdn + '31097/1.0', },
    'forsenDDK': { src: twitch_cdn + '36391/1.0', },
    'forsenMoney': { src: twitch_cdn + '36392/1.0', },
    'forsenBanned': { src: twitch_cdn + '36394/1.0', },
    'forsenAbort': { src: twitch_cdn + '36536/1.0', },
    'forsenSS': { src: twitch_cdn + '36535/1.0', },
    'forsenX': { src: twitch_cdn + '60257/1.0', },
    'forsenClown': { src: twitch_cdn + '60378/1.0', },
    'forsenC': { src: twitch_cdn + '60379/1.0', },
    'forsenSheffy': { src: twitch_cdn + '60390/1.0', },
    'forsenPuke': { src: twitch_cdn + '60391/1.0', },
    'forsenPepe': { src: twitch_cdn + '60279/1.0', },
    /* Nymn Emotes */
    'nymnSave': { src: twitch_cdn + '63020/1.0', },
    'nymnW': { src: twitch_cdn + '62338/1.0', },
    'nymnPepe': { src: twitch_cdn + '62456/1.0', },
    'nymnC': { src: twitch_cdn + '63891/1.0', },
    'nymnWeeb': { src: twitch_cdn + '64154/1.0', },
    'nymnGasm': { src: twitch_cdn + '63893/1.0', },
    'nymnGun': { src: twitch_cdn + '63896/1.0', },
    'nymnXAXA': { src: twitch_cdn + '63890/1.0', },
    /* BTTV - Global */
    'FeelsBadMan': { src: bttv_cdn + '55678c247239dcf87b80d78b/1x', },
    'FeelsGoodMan': { src: bttv_cdn + '55678f9b7239dcf87b80d791/1x', },
    'KKona': { src: bttv_cdn + '54fb961b01abde735115de01/1x', },
    'SourPls': { src: bttv_cdn + '550293fd135896936880fdfd/1x', },
    '(puke)': { src: bttv_cdn + '550288fe135896936880fdd4/1x', },
    /* BTTV - User */   
    'forsenPls': { src: bttv_cdn + '55e2096ea6fa8b261f81b12a/1x', },
    'gachiGASM': { src: bttv_cdn + '55999813f0db38ef6c7c663e/1x', },
    'gachiLEATHER': { src: bttv_cdn + '55999d0ff0db38ef6c7c6646/1x', },
    'gachiPls': { src: bttv_cdn + '55ede2ea63ddc12253e62dd9/1x', },
    'justDOIT': { src: bttv_cdn + '559f4d1cae90d55f200399fa/1x', },
    'KKonaPls': { src: bttv_cdn + '55a24e1294dd94001ee86b39/1x', },
    'PepePls': { src: bttv_cdn + '55898e122612142e6aaa935b/1x', },
    'RareParrot': { src: bttv_cdn + '55f049e704c1cb790ade6292/1x', },
    '(ditto)': { src: bttv_cdn + '554da1a289d53f2d12781907/1x', },
};
$(document).ready(function() {
    for (i in emotes) {
        var emote_code = i;
        emote_code = emote_code.replace(new RegExp('\\(', 'g'), '\\(');
        emote_code = emote_code.replace(new RegExp('\\)', 'g'), '\\)');
        emotes[i].regex = new RegExp('((?![^ ]).{1}|^.{0})' + emote_code + '(?![^ ])', 'g');
    }

    $('.pemote').each(function(index, el) {
        for (i in emotes) {
            $(el).html($(el).html().replace(emotes[i].regex, ' <img src="'+emotes[i].src+'" alt="'+i+'" title="'+i+'"/>'));
        }
    });
});
