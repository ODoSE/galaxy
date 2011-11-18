#!/usr/bin/env python
'''
Module to submit errors to FogBugz automatically.

@author: tbeek
'''

import urllib
import urllib2
import sys
import traceback

def report_error_to_fogbugz():
    '''From an except-clause retrieve details about the error and post the results to FogBugz'''
    desc, lines = get_error_trace_lines()
    return post_to_fogbugz(description = desc, extra_info = lines)

def get_error_trace_lines():
    '''For the current error return an ID line & string containing a complete stacktrace and local variables.'''
    err, value, trace_back = sys.exc_info()
    lines = []
    while trace_back:
        #Walk through trace_back to get all frames
        frame = trace_back.tb_frame
        trace_back = trace_back.tb_next

        #Identify frame
        lines.append("Frame %s at %s:%s" % (frame.f_code.co_name,
                                            frame.f_code.co_filename,
                                            frame.f_lineno))
        #Get locals in frame
        for key in sorted(frame.f_locals.keys()):
            #Calling str() on an unknown object could cause an error we don't want: Prevent that.
            try:
                value = frame.f_locals[key]
            except:
                value = "<ERROR CALLING STR() ON %s>" % key # pylint: disable-msg=W0702
            lines.append("\t%20s = %s" % (key, value))
        #Separator between this frame and the next
        lines.append('\n')

    #Append nicely formatted stack trace 
    lines.extend(traceback.format_exc().splitlines())

    #Get error desciption as Type(values) @ file:line
    description = '{0} @ {1}:{2}'.format(err.__name__, frame.f_code.co_filename, frame.f_lineno)
    return description, '\n'.join(lines)

def post_to_fogbugz(description = 'Bug report from Galaxy',
                    extra_info = '',
                    user = 'Tim te Beek',
                    project = 'BRS2010P33 Genome-wide signatures of adaptive divergence in bacteria',
                    area = 'Misc',
                    correspondent = 'brs@nbic.nl',
                    force_new = '0',
                    friendly = '1',
                    MESSAGE = 'Thank you, your bug report has been received.',
                    fogbugz_url = 'https://brs.fogbugz.com/scoutSubmit.asp'):
    '''Post a MESSAGE to FogBugz using the ScoutBugz HTTP POST interface.'''
    values = {
        "ScoutUserName":user,
        "ScoutProject":project,
        "ScoutArea":area,
        "Email":correspondent,
        "ScoutDefaultMessage": MESSAGE,
        "FriendlyResponse":friendly,
        "ForceNewBug":force_new,
        "Description":description,
        "Extra":extra_info}

    #Post error to fogbugz
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(fogbugz_url, data)
        response = urllib2.urlopen(req)
        content = response.read()
        return content
    except:
        #Do not mask original error by an error in posting to FogBugz
        return 'failed to post MESSAGE' # pylint: disable-msg=W0702

if __name__ == '__main__':
    try:
        raise Exception('bla')
    except:
        print report_error_to_fogbugz()
        raise
