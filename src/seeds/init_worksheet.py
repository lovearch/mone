#!/usr/bin/env python
#encoding=utf-8
from _django_orm import *
#工单类型
worksheet_type_list = [("申请ECS服务器", "<p>项目名称：</p><p>服务器使用目的：</p><p>负责人：</p><p>CPU/核：</p><p>内存/G：</p><p>硬盘/G(服务器自带40G系统盘，默认不创建数据盘)：</p>"
                             "<p>网络带宽(不需要则填无；需要请填写原因)：</p><p>数量/台：</p><p>购买时长/月：</p>"),
                 ("申请RDS服务器", "<p>项目名称：</p><p>服务器使用目的：</p><p>负责人：</p><p>数据库名：</p><p>账户名：</p><p>内存/M：</p><table border='1'>"
                             "<thead><tr><th>内存/M</th><th>240</th><th>600</th><th>1200</th><th>2400</th><th>6000</th><th>12000</th><th>24000</th><th>48000</th></tr></thead>"
                             "<tbody><tr><td>最大连接数</td><td>60</td><td>150</td><td>300</td><td>600</td><td>1500</td><td>2000</td><td>2000</td><td>2000</td></tr>"
                             "<tr><td>最大IOPS</td><td>150</td><td>300</td><td>600</td><td>1200</td><td>3000</td><td>6000</td><td>12000</td><td>14000</td></tr></tbody>"
                             "</table><p>硬盘/G：</p><p>是否开通外网(不需要则填无；需要请填写原因)：</p><p>添加白名单服务器：</p><p>数量/台：</p><p>购买时长/月：</p>"),
                 ("申请SLB负载均衡", "<p>项目名称：</p><p>服务器使用目的：</p><p>负责人：</p><p>网络带宽(不需要则填无；需要请填写原因)：</p><p>后端服务器：</p>"
                              "<p>监听协议(tcp监听/http监听/https监听/udp监听)：</p><p>TCP监听前端端口号：</p><p>TCP监听后端端口号：</p>"
                              "<p>转发规则(加权轮询/加权最小连接数)：</p><p>会话保持是否开启：</p><p>数量/台</p>"),
                 ("ECS配置变更", "<p>项目名称：</p><p>负责人：</p><p>ECS的ip：</p><p>变更CPU/核：</p><p>变更内存/G：</p><p>变更硬盘/G：</p><p>变更网络带宽：</p><p>变更原因：</p>"),
                 ("RDS配置变更", "<p>项目名称：</p><p>负责人：</p><p>RDS的id：</p><p>内存/M：</p><table border='1'>"
                            "<thead><tr><th>内存/M</th><th>240</th><th>600</th><th>1200</th><th>2400</th><th>6000</th><th>12000</th><th>24000</th><th>48000</th></tr></thead>"
                            "<tbody><tr><td>最大连接数</td><td>60</td><td>150</td><td>300</td><td>600</td><td>1500</td><td>2000</td><td>2000</td><td>2000</td></tr>"
                            "<tr><td>最大IOPS</td><td>150</td><td>300</td><td>600</td><td>1200</td><td>3000</td><td>6000</td><td>12000</td><td>14000</td></tr></tbody></table>"
                            "<p>硬盘/G：</p><p>是否开通外网：</p><p>变更原因：</p>"),
                 ("SLB配置变更", "<p>项目名称：</p><p>负责人：</p><p>SLB的ip：</p><p>网络带宽：</p><p>后端服务器：</p><p>TCP监听前端端口号：</p><p>TCP监听后端端口号：</p>"
                            "<p>转发规则(加权轮询/加权最小连接数)：</p><p>会话保持是否开启：</p><p>变更原因：</p>"),
                 ("反向代理配置", "<p>项目名称：</p><p>负责人：</p><p>域名：</p><p>后端ECS的ip：</p><p>会话保持是否开启：</p>"),
                 ("SQL执行", "<p>项目名称：</p><p>负责人：</p><p>RDS的id：</p><p>数据库名：</p><p>账户名：</p><p>SQL执行原因：</p>"),
                 ("白名单添加", "<p>项目名称：</p><p>负责人：</p><p>RDS的id：</p><p>添加白名单ECS的ip：</p><p>白名单添加原因：</p>"),
                 ("表库迁移", "<p>项目名称：</p><p>负责人：</p><p>源库、源表：</p><p>目标库、目标表：</p><p>表库迁移原因：</p>"),
                 ("数据库创建", "<p>项目名称：</p><p>负责人：</p><p>RDS的id：</p><p>数据名：</p><p>账户名：</p><p>添加白名单ECS的ip：</p><p>数据库使用目的：</p>"),
                 ("域名申请", "<p>项目名称：</p><p>负责人：</p><p>新增域名：</p><p>解析类型(A/CNAME或其他)：</p><p>解析内容：</p><p>域名使用目的：</p>"),
                 ("域名变更", "<p>项目名称：</p><p>负责人：</p><p>原域名：</p><p>变更原域名：</p><p>变更解析类型(A/CNAME或其他)：</p><p>变更解析内容：</p><p>域名变更目的：</p>"),
                 ("CDN加速", "<p>项目名称：</p><p>负责人：</p><p>静态资源域名：例如{app}.res.meizu.com</p><p>备注：附件中提交静态资源服务器nginx配置文件</p>"),
                 ("新增应用", "<p>新增应用名称：</p><p>负责人：</p><p>申请ECS服务器：</p><p>申请RDS服务器：</p><p>申请SLB负载均衡：</p><p>域名申请：</p><p>CDN加速：</p><p>git地址：</p><p>构建地址：</p><p>正式构建环境构建命令：</p>"),
                 ("应用下线", "<p>下线应用名称：</p><p>负责人：</p><p>下线ECS的ip：</p><p>下线RDS的id：</p><p>下线数据库名称：</p><p>下线SLB的ip：</p><p>下线域名(包括静态资源域名)：</p><p>下线原因：</p>"),
                 ("其他", "")]
worksheet_type_model_list = [WorksheetType.objects.create(name=name,template=template) for name,template in worksheet_type_list]