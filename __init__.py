# Copyright 2016 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import webbrowser

from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


# TODO - Localization

class SearchSkill(MycroftSkill):
    @intent_handler(IntentBuilder("").require("Search").require("Words"))
    def default(self, message):
        """
            TODO: The method is very english centric and will need
                  localization.
        """
        utterance = message.data.get('utterance')
        keyword = re.sub('^.*?' + message.data['Search'], '', utterance)
        # self.speak(repeat.strip())
        url = 'https://cn.bing.com/search?q=' + keyword.strip()
        webbrowser.open(url)

    def stop(self):
        pass


def create_skill():
    return SearchSkill()
