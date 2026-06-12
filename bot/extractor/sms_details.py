import re
import random

class SMSDetails:

    def __init__(self, text: str) -> None:
        self.text = text
        self.pattern = re.compile(
            r"USER:\s*(?P<user>.*?)\n\s*(?:EMAIL:\s*(?P<email>.*?)\n\s*)?SID:\s*(?P<sid>.*)\n\s*PHONE:\s*(?P<phone>.*)\n\s*Message:\s*(?P<message>.*?)(?:\n\s*Image:|$)",
            re.DOTALL | re.IGNORECASE
        )
        self.sid = ''

    def text_match(self) -> bool:
        return  self.pattern.search(self.text)

    def crop_out_content(self) -> str:
        match = self.text_match()
        if match:
            extracted_content = {
                'phone_number': match.group('phone').strip(),
                "message" : match.group("message").strip(),
                "sid": match.group('sid').strip()
            }

            return extracted_content
            
    def sms_details_composer(self) -> str:
        sms_details = self.crop_out_content()

    
        if sms_details['phone_number']:  
            
            try:
                fixed_number = sms_details['phone_number'].replace(' ', ',')

                phone_number_list = list(map(str, fixed_number.split(',')))

                digits = list(phone_number_list[0])
                positions = [i for i, c in enumerate(phone_number_list[0]) if c.isdigit()]
                for i in positions[-5:]:
                    digits[i] = str(random.randint(0, 9))

                sid =  ''.join(digits)

                if sms_details['sid'] == '' or sms_details['sid'] == 'None':
                    self.sid = sid
                else:
                    self.sid = sms_details['sid']


                return {
                    'phone_number': fixed_number,
                    "message" : sms_details['message'],
                    "sid": self.sid
                }
                
            except ValueError:
                return "Error: Caption contains non-numeric values."
        else:
            return 'Not Found'
        
            
           