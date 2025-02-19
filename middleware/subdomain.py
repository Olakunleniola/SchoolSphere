import ipaddress


class SubdomainMiddleware:
    """
    Extracts the subdomain from the HTTP host.
    For example, for binta-schools.lvh.me, request.subdomain will be 'binta-schools'.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Remove port
        try:
            ipaddress.ip_address(host)
            request.subdomain = None
        except:        
            parts = host.split('.')
            # For lvh.me, host parts are [subdomain, 'lvh', 'me'] if subdomain exists.
            if len(parts) >= 3:
                request.subdomain = parts[0]
            else:
                request.subdomain = None
        return self.get_response(request)
