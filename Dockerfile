FROM wordpress:latest
WORKDIR /var/www/html
COPY ~/covid19-vaccine/conf/portsconf.txt /etc/apache2/ports.conf
COPY ~/covid19-vaccine/conf/siteenable.txt /etc/apache2/sites-enabled/000-default.conf
ADD cmd.sh /
RUN chmod +x /cmd.sh
CMD ["/cmd.sh"]
