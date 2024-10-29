# Sử dụng base image cho Python của AWS Lambda
FROM public.ecr.aws/lambda/python:3.10

# Cài đặt các thư viện hệ thống cần thiết cho Google Chrome
RUN yum install -y \
    wget \
    unzip \
    chromium \
    fontconfig \
    google-chrome-stable \
    && yum clean all

# Cài đặt webdriver_manager
COPY requirements.txt .
RUN pip install -r requirements.txt

# Sao chép mã nguồn vào container
COPY . ${LAMBDA_TASK_ROOT}

# Command mặc định của Lambda container
CMD ["lambda_function.lambda_handler"]
