# 环迅
ips_login_url = "http://merchant.ips.com.cn/Login.aspx?logType=1"
ips_merchant_id = "txtMerchantCode"
ips_user_name_id = "txtUserName"
ips_password_id = "txtUserPwd"

ips_validate_Code_id = "txtValidateCode"
ips_warn_xpath_string = "//span[@id='lbWarning']"

ips_login_button_id = "btnLogin"

ips_security_login_class_name = "big1"
ips_ordinary_admin_id = "rdNormal"
ips_image_xpath_string = "//img[@src='img.aspx']"

ips_merchant_dic_dir = "dictionary/merchant_code_dic"
ips_user_name_dic_dir = "dictionary/user_name_dic"
ips_password_dic_dir = "dictionary/user_pwd_dic"

ips_tessdata_dir = "F:/software/tesserOcr/tessdata/."

# 惠农
hn_login_url = "https://wxbank.ynhtbank.com/euler-tld/#login"
hn_user_name_id = "userName"
hn_password_id = "password"
hn_login_button_id = "login"
hn_warn_string = "//span[@id='errorMessage']"
hn_error_message = {'ENUP': "用户名或密码错误", 'ENU': "请输入帐号/别名/邮箱/手机号",
                    'ENP': "请切换英文输入法输入密码"}

hn_user_name_dic_dir = "dictionary/phone_number_dic"
hn_password_dic_dir = "dictionary/user_pwd_dic"

ke_login_url = "https://login.ke.com/login?service=http://saas.realsee.com/login?gotoURL=%252F"
ke_user_name_id = "username"
ke_password_id = "password"
ke_login_button_class_name = "btn-login"
ke_warn_string = "//class[@class='frame-p-error-msg']"

ke_error_message = {'ENUP': "用户名或密码不正确"}
ke_username_dic_dir = "dictionary/phone_number_dic"
ke_password_dic_dir = "dictionary/user_pwd_dic"

ali_password_id="password_rsainput"
ali_user_name_xpath="//input[@seed='formItem-account']"
ali_login_button_xpath="//input[@seed='formItem-btn']"
ali_login_url="https://auth.cloud.alipay.com/authorize?clientId=LTAIphRJ2ntlkoTA&responseType=code&grantType=authorizationCode&redirectUri=https://mappcenter.cloud.alipay.com/index.htm"
ali_warn_string="form-error"
ali_error_message = {'ENUP': "账户名格式错误"}