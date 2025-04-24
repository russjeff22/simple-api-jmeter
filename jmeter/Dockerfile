FROM justb4/jmeter:5.5

# Copy your test plan into the container
COPY simple-api-test.jmx /test/simple-api-test.jmx

# Run JMeter in non-GUI mode with the test plan
CMD ["-n", "-t", "/test/simple-api-test.jmx", "-l", "/test/results.jtl"]