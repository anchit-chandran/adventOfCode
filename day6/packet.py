class Packet:
    def __init__(self, packet):
        self.packet = packet
        self.start_pointer = 0
        self.end_pointer = 1
        self.seen = set([self.packet[self.start_pointer], self.packet[self.end_pointer]])

    #getters
    def get_start_pointer_val(self):
        return self.packet[self.start_pointer]
    def get_end_pointer_val(self):
        return self.packet[self.end_pointer]
    def get_seen(self):
        return self.seen
    
    #check if values are same, return True if not
    def check_same(self):
        return self.packet[self.start_pointer] == self.packet[self.end_pointer]
    
    # increase pointer by 1
    def push_start(self):
        self.start_pointer+=1
        self.set_seen()
    def push_end(self):
        self.end_pointer+=1
        self.prev_seen = self.seen
        self.set_seen()
        # check if duplicate letter seen. If so, push window 1
        if len(self.prev_seen) == len(self.seen):
            self.push_start()
            self.end_pointer = self.start_pointer + 1
            self.set_seen()

    def push_window(self):
        self.push_start()
        self.push_end()
    
    #add seen
    def set_seen(self):
        self.seen = set(self.packet[self.start_pointer:self.end_pointer])
    
    # check if found 4 unique letters
    def seen_14(self):
        return len(self.seen) == 14
    
    #pprint packet and pointer positions
    def show_pos(self):
        i = self.packet
        print(f"Seen: {self.get_seen()}")
        print(f"{i[:self.start_pointer]} >|{self.get_start_pointer_val()}{i[self.start_pointer+1:self.end_pointer]}{i[self.end_pointer]}|< {i[self.end_pointer+1:]}")

i = "pwjwljjjvqjqjzqjqvvpgvpggmdgdrrzmzfzmzffzbbjnbjnjddsdpsdsgsgvsgvgmmzvvpspvspsdsbsbffhwhlwwzllftfhhrfrsrrnnngqgtglgfgtffnssrspsqppdvdtdwwpfpzffnpnddvsswjswjjhdjdrjrwwfpwfpfjppzwzvzpzrznzgzcgzgpgfpffwggtbbhsslzztpplltdtqtctrrszrzszpsprptrtgrtrzrvzrvzrrsfsbswsvvbdbjjgljjwqwgqwwtmwwnbbzdbdwwsnntztstbssnjssjmmldmmrrnfrfgfbbszzzlrrwzwtwwbrwrlwrwzwmwqmwwtqwwtvvdqdtqqfnfjnjsnslltcllvmmdmttvsszrsrwssdmdttdmdrmrsrvrllrhlltmlmlzmlzzhvhbbflfsslclpcczmmcjmjccpgprrgnrrzqqmgqggfvgffbsfsbfbttrgtrtptgtjtnnfbfmmrrcmcwwbbmwmvvvtppslsvvlsvswwztwztzqqpggdccmlldlplggrgddlrddvwvsswllsffbllsbbslshslswsllnqlqrqqpmqmtmqtmqtmmbwmbbzdbzbttvptvpvgpvggblbsspgppvmvsswfssfdfrdffpbfpprmrssmbbmggszslzlslblsldsldssjjsrjjjdfdjdtdmdnnncddpfddrjdjvjfvjffftmfmqqqqqfjjhssbzbbfjjmmzgzllphlplhlplfpfnpnsppjjqsshpssjdjzzwvvjfvfnfttmtbbgtgbbdpbbjppzcpzzvcvpvvdcvvcfvvfsvsccmhhrwrjjsrjrvrfvfwvvtftzztlztlthlhrhnnlpnllnmnfmffzpffhlhbhqbhqhfhwwlglnndgdwdswwgtwgtgsttpbprpqpnnbsnbsnszzrszsqzqlqggvhghrrvprvvvqnnmmrwrbrrmttwrrlmrrrddmsddbhdhdjhdhrhffppphghvvtztptjjlppcqcscjscstsmsbspsgpgqgmmndmdvvpnpnrrjtrthhtzzjlzzrwzrrfsfflrrmffhlhglhhhhvwwttlcttbqqzzbzzzbhbsscqqjggqpggqffbttrfrjjjqmmpttlvvqlvqqqtgtrtcrcbcnbbhfbfhbhqbhqbqvbvqvrqvvgttqwqpwqwnnpgngpphjppztptnnrssjqqrplzrvmwmbrbgbnggvzpmphqsrjrdhtslpmmwrhgcndwtbsbrfmsplzqswsnmrwdwwhzmpbqcmjfsmnwqnjmvdczhgmtfjwnjfdllfzdwpwgclpbdqtqnqqqvpthltznfzshhgrwwqclpplmdwtpjszrdwwzfbljcjmqmhptfhvcbvgfjfftbsfglwqldphdzzgcmvtsbhlsdncfjcsqrqrtdhttcwzlbqhvgppbrjfzdzwzprwpfflmdspcmqcbdhsvwjswwbzwnqrshbqfnmtdzrsrjgqngntllcgwjnmjqvtgwvttfqrcjlhbpcrszlngfmdgzprcdttgbjpcdzbhtdghpltcbvcddnslhqthfvzjtspqlzhdprhgtrlqqgtsqwwjqthgdwfgdfzhrnrwlrpqmgqltgldpjqgjzvngrphclbfftnwfnfvsvhftthptqfnvlftdpdhcrjdhfwtpwwvsblgntdwcpnsprhnpjtjsprdrdjwlhnmnzmmjmcdfsctzgmlqwwrwztjndqgpqrvdgplcnntqhfjlzjszpdwnvlwdzzgpzvplglgrmsjgjpmsrdsgzlfblgbgszgdtgsggqvhzmnfcnvlnzrfpqphctlcqccqzslmlsbbztnpncqpgscgdmmsgfwqrzpmbqrmfqsnnggswhmgmtmgdmhwthbgbdsrtnsrvdfdhlhhczgdsdqnpsgjzpbnsmgrvsfdjlhgjfjjwqnrnrbzdzcjlstclpqfnrflgnzbdbzvbjcbgqrrrlfcpgptcghhqqfsvsgljvjhdgdgcjtnrqsctmwhzbmbrfrsvndhfrtwlfgvqcbjsvttrctfshrggdvgbhthnwbwqglrvfbsqnbhdwgzhbccjnlhtcbjlpgrvttthnwvvspnzvqhjvmtwshcstdjhfqhqcgvwqwwwwrfdmnjhldsrhgmtjddsghdmdrpczbcjflmbhszctmvdttfrrqqpwslhvqbjlsrjdjrcqjrhwgjlsqmvdpvvvlbzwtthptpsggddcbqbhrvrpdtncvgndclhpngzgfqdqgwwbrjltjtqbpbtbzjmfmnjnlqmtzvdqdwqhbgptplrgdsfpjzfrpdcdsznwffpnzsmpqjfbcpddqjgfqhqbwsfmzgstfdnzhphhvgbzvjrlmqmrznpctftcmbtdpbfbfpfpjtjhbcrrssnlvtrtnzvwtjwplclpqndpfstjmghmzsllhntprtjwlppjnjgjzlvlcbcwjvrjqjhfnnpmwlpngwtvvbcllmjzqfrwvtvsrvbcpfwcdfwmdwvztwtbrgvlvmfjmpzdzmfbcmrsqfwqjfjfrgmnblnzfzcvgwllvmqfmdlqqgvvjrptlrjcwphvchwhmtwhnlnjprqhlrhmdfptvpshjbzrhptvnqfvjfjcnglnbfhbwghqqjbqzdthjwqzznwfsmqmbsqnwrdrrwjgzjdmgtsqswlqcpshdmcfjttpszqmsjhgfsrvgchgwzbqgbdqhmbndmnmwjsnjjvmtpprbtlwzpvfdnbtjnzzvlwndgbhgwbpllvfghwvwjmlpnzfjzjwwmtvbbfndppbqwhjlwgtswmgffddbhnwqljvgcvfnqmzgvfmjwsbcrpgtcpchlblccgpgpmddsjsfwbnvnsfttnsqjshchdztvsbjwsfmszfwpwsmgzvvcfddtczvvmnhgjffrsfqzfmphpfblmwgcbbrjqzdztzzzjhqmjzrgmwgrqdfqdbjsgwfndqgnmdvjlwdtjpjtpcqlhtcfvnmzjswldrbqjpmrlqwhvnqjshbqqvzwwsdjmspgbvrgvpjjnwsvnvnppvlnqbdllfczjjftpnlrjfvcwgwbdmldtcnczqzcptjjrgglnnbgmrdffgmnnwvjzwbgcncnhzmthswrdsrhchprrrrnhjfnzmsgfjltqzmttvhslnsgcjfgqwcsddfstcstspcpdbznvdrnqhwqsfgqtdbtwspfswfjbzgtqjpvzfhfdblszblmgrmmlwvnwwdsdjjvrsfjfjltcsfccplftvpltqshgnpnqlqcglrhvzldptspnbvjcchnnvzvbbqnnnbnggrhpcgqtgnjdqplswtblgtwqzmltjjhpdttgbcvhfrsdcgjzswvtbbhrpnzmrjhgznbdpqgqdhwcnmgflpdtbzdbvzvslbvvwdpcnwjtvjhgncnljfwlrvqgdrjhdcprsqjrmwwlcrrvsjtlmqmjtcbqwcbmgnvfshdgmmfffzvwjphjfspvdzjsqdlgqfdjwwshdcssqvvgdcvvtmwlfjdvtfllrvltmrsgpdtdqsfjpcvjnqszpnbqqlnpdvhtswbgwnpcqpgzqwlgsmlnlngcdmqhchcdgfmrhfwwrgrrdrhcsbbcrhghdjrcsltchqghvmbvbbpqzqbgwmqrgwchhbvdsqbqrfcbzwjrlqtnmghtjbtjdpngcjzswfmjfphjnftbhdgvwjsvqfbsfgqhfbcrgrsppsvbnpwlhsdrffcmmgzpjfsvllcrbtwrwddthfjvjndzfzbcmglhbzpzwwbtzdpdlwrnbzqjbqwpbdlwfddbtzjhqshmcghqfcrzrmrtmqwpqhvqzbfwhbssgjcmzqcpvnntbpfqwhbmtjdtbtrrdhsvzqjltdshtlvwwmlbdzlvjhmtppnbqcjnncpslcggsjbrmzvdgqzclwszgzfqthndnjfjrznlmmtjwwhnzvhnjncccpczrftvhtdhjbzvwvlgqhdnfqdqrhctfffpcnqzdrgqqzcczdjvpzqfgfcpjzqhbwshsqhvqzpsb"
print(len(i))
s = Packet(packet=i)
while not s.seen_14():
    # user_input = input('->>')
    s.push_end()
    # s.show_pos()
    # s.show_pos()
    # print(f"Currently at: {s.counter}. Seen 4 unique characters previously: {s.seen_4()}")
print(f"Answer={s.end_pointer}")
