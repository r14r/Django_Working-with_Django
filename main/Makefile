PREFIX_PKG := working-with-django

BOOTSTRAP_VERSION := 4.4.1
BOOTSTRAP_DEST    := static/vendor/bootstrap

default:
	grep -E ':\s+#' Makefile

clearcache:	# Clear Cache
	python3 manage.py clearcache

run:		# Run Server
	python3 manage.py runserver 8000

deploy:		# Deploy
	rm -rf dist $(PREFIX_PKG)*
	rm -rf polls.dist
	cd polls && python3 setup.py sdist
	mkdir polls.dist && mv polls/dist/* polls/$(PREFIX_PKG)* polls.dist


jquery_install:		# Install jQuery Library
	cd .. && yarn add jquery
	rm -rf polls/static/jquery
	mkdir  polls/static/jquery
	cp ../node_modules/jquery/dist/* $(JQUERY_DEST)

bootstrap_install:	# Install Bootstrap Library
	cd .. && yarn add bootstrap
	rm -rf  polls/static/bootstrap
	mkdir   polls/static/bootstrap
	cp -R ../node_modules/bootstrap/dist/* $(BOOTSTRAP_DEST)

bootstrap_download:	# Install Bootstrap from Source
	mkdir -p install/bootstrap
	wget -q https://github.com/twbs/bootstrap/releases/download/v$(BOOTSTRAP_VERSION)/bootstrap-$(BOOTSTRAP_VERSION)-dist.zip -O install/bootstrap/$(BOOTSTRAP_VERSION).zip
	#
	mkdir -p                                                     $(BOOTSTRAP_DEST)
	rm -rf                                                       $(BOOTSTRAP_DEST)/bootstrap-$(BOOTSTRAP_VERSION)-dist
	unzip -q install/bootstrap/$(BOOTSTRAP_VERSION).zip       -d $(BOOTSTRAP_DEST)
	mv $(BOOTSTRAP_DEST)/bootstrap-$(BOOTSTRAP_VERSION)-dist     $(BOOTSTRAP_DEST)/$(BOOTSTRAP_VERSION)

