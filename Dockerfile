FROM wordpress:latest
WORKDIR /var/www/html
COPY portsconf.txt /etc/apache2/ports.conf
COPY siteenable.txt /etc/apache2/sites-enabled/000-default.conf
ADD cmd.sh /
RUN chmod +x /cmd.sh
CMD ["/cmd.sh"]
