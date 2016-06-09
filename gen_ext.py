import os
import random
import string

def generate():
    ext_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    ext_name = 'axl' + ext_key
    ext_id = 'axl' + ext_key + '@mozilla.org'

    os.system('rm webext/*')
    os.system('rm *.xpi')

    manifest = open('webext/manifest.json', 'w')
    manifest.write('{"manifest_version": 2, "name": "' + ext_name + '", "version": "1.0", "description": "Aides in efforts to improve automation testing in Firefox Add-ons.", "applications": { "gecko": { "id": "' + ext_id + '", "strict_min_version": "45.0" } }, "content_scripts": [ { "matches": ["*://justinpotts.github.io/webext-gen-frontend/test?key=' + ext_name + '"], "js": ["genext.js"] } ] } ')
    manifest.close()

    genextjs = open('webext/genext.js', 'w')
    genextjs.write('document.getElementById(\'indicator\').innerHTML = \'<p><img id="success" src="media/img/check-mark.jpg"></p><p><span class="download-completion">It works!</span></p><p><span class="install-instructions">To disable or remove the add-on, visit about:addons.</span></p>\';')
    genextjs.close()

    os.chdir('webext')
    os.system('zip -r ../' + ext_name + '.xpi *')
    os.chdir('../')

    return ext_name
