from Resource import Resource

class Reports (Resource):

    def __init__(self, host, username, passwd):
        return super(Reports, self).__init__(host, "/reports", username, passwd)

    def report(self,
               url,
               queues,
               format   = "",
               start    = None,
               end      = None,
               sysmsg   = False,
               notanswered   = False,
               duration = None,
               timezone = None):
        data = {'queues'   : ','.join(queues),
                'format'   : format,
                'start'    : start,
                'end'      : end,
                'sysmsg'   : sysmsg,
                'notanswered'   : notanswered,
                'duration' : duration,
                'timezone' : timezone
                }
        data = dict([(k, v) for k, v in data.iteritems() if v is not None])
        if format != 'csv':
            data.pop('format')

        response = self.httpRequest('GET', url = url, params = data)
        return response, response.status_code

    def chatsPerHour(self,
                     queues,
                     format   = "",
                     start    = None,
                     end      = None,
                     sysmsg   = False,
                     duration = None,
                     timezone = None):
        return self.report("/chats-per-hour", queues,
                           format   = format,
                           start    = start,
                           end      = end,
                           sysmsg   = sysmsg,
                           duration = duration,
                           timezone = timezone)
    
    def chatsPerMonth(self,
                     queues,
                     format   = "",
                     start    = None,
                     end      = None,
                     sysmsg   = False,
                     notanswered   = False,
                     duration = None,
                     timezone = None):
        return self.report("/chats-per-month", queues,
                           format   = format,
                           start    = start,
                           end      = end,
                           sysmsg   = sysmsg,
                           notanswered   = notanswered,
                           duration = duration,
                           timezone = timezone)
    

    def chatsPerProtocol(self,
                        queues,
                        format   = "",
                        start    = None,
                        end      = None,
                        sysmsg   = False,
                        notanswered   = False,
                        duration = None,
                        timezone = None):
        return self.report("/chats-per-protocol", queues,
                           format   = format,
                           start    = start,
                           end      = end,
                           sysmsg   = sysmsg,
                           notanswered   = notanswered,
                           duration = duration,
                           timezone = timezone)
    

    def chatsPerQueue(self,
                        queues,
                        format   = "",
                        start    = None,
                        end      = None,
                        sysmsg   = False,
                        notanswered   = False,
                        duration = None,
                        timezone = None):
        return self.report("/chats-per-protocol", queues,
                           format   = format,
                           start    = start,
                           end      = end,
                           sysmsg   = sysmsg,
                           notanswered   = notanswered,
                           duration = duration,
                           timezone = timezone)
    
    def chatsPerOperator(self,
                        queues,
                        format   = "",
                        start    = None,
                        end      = None,
                        sysmsg   = False,
                        notanswered   = False,
                        duration = None,
                        timezone = None):
        return self.report("/chats-per-protocol", queues,
                           format   = format,
                           start    = start,
                           end      = end,
                           sysmsg   = sysmsg,
                           notanswered   = notanswered,
                           duration = duration,
                           timezone = timezone)
    
