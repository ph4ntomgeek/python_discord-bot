import csv
curse_words = [
  
'Fuck', 'F*ck', 'Fu*k', 'Fuc*', 'fuck', 'f*ck', 'fu*k', 'fuc*', 'Asshole', 'asshole', 'A*shole', 'a*shole', 'A**hole', 'a**hole', 'bloody', 'Bloody', 'bl*ody',
'*loody', 'b*oody', 'cunt','c*nt', 'C*nt', '4r5e',  '5h1t', '5hit',  'a55', 'anal',  'anus',  'ar5e',  'arrse',  'arse',  'ass',  'a_s_s',  'b!tch', 'b00bs', 'b17ch', 'b1tch', 'bastard', 'bi+ch', 'biatch', 'bitch', 'bloody', 'blow job', 'blowjob', 'bum',  'butt', 'c0ck',  'c0cksucker', 'boob',  'boobs',  'booobs',  'boooobs',  'booooobs',  'booooooobs',  'breasts', 'dick', 
'd1ck', 'dildo', 'cnut', 'cock', 'crap', 'cum', 'cox', 'coon', 'sex'
 , 'gay', 'bastard', 'pimp', 'hoe', 'dick', 'choad', 'Twat', 'pussy',  'vagina', 'Vagina', 'porn', 'Porn', 'hoe', 'Hoe', 'slut', 'stud', 'Blowjob','dlck',  'dog-fucker', 'doggin', 'dogging',  'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculat', 'ejakulate', 'f u c k', 'f u c k e r', 'fuk', 'fuker', 'fuk',  'fux', 'f_u_c_k', 'gangbang',
  ]
file = open('swearWords.csv')
type(file)
csvreader = csv.reader(file)
header = next(csvreader)
file.close()
for element in header:
 curse_words.append(element)
