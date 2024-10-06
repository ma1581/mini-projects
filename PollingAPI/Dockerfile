# Use a base image with both Java 17 and MariaDB
FROM openjdk:17

# Set the working directory
WORKDIR /app

# Copy the JAR file from the local build context to the container
COPY target/PollingApp-0.0.1-SNAPSHOT.jar /app/

# Set environment variables for MariaDB
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=pollapp
ENV MYSQL_USER=ma1581
ENV MYSQL_PASSWORD=1581

# Expose the default MySQL port
EXPOSE 3306

# Copy SQL script to initialize the database
COPY ./sql-scripts/init.sql /docker-entrypoint-initdb.d/

# Command to run the Spring Boot application
CMD ["java", "-jar", "PollingApp-0.0.1-SNAPSHOT.jar"]
