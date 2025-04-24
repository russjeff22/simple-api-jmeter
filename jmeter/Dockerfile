FROM justb4/jmeter:5.5

# Copy the test plan into the container
COPY simple-api-test.jmx /test/simple-api-test.jmx

# Run JMeter in non-GUI mode
CMD ["jmeter", "-n", "-t", "/test/simple-api-test.jmx", "-l", "/test/results.jtl"]
