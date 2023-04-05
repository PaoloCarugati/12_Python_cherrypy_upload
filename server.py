import os
import cherrypy

config = {
    'global' : {
        'server.socket_host' : '127.0.0.1',
        'server.socket_port' : 8080
    }
}


class App:

    @cherrypy.expose
    def upload(self, ufile):
        #salvo il file nella cartella corrente
        upload_path = os.path.dirname(__file__)
        #lascio il nome del file inalterato
        upload_filename = ufile.filename
        #ottengo il percorso completo del file (percorso + nome file)
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        
        size = 0
        #apro il file (stream)
        with open(upload_file, 'wb') as out:
            #faccio la lettura a blocchi (chunk)
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
File ricevuto.<br />
Nome File: {}<br />
Dimensione: {}<br /> 
Mime-type: {} bytes
''' .format(ufile.filename, size, ufile.content_type, data)
        return out


if __name__ == '__main__':
    cherrypy.quickstart(App(), '/', config)