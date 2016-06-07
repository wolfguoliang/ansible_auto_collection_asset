#!/usr/bin/env python
# coding=utf-8
# author ：wosun
gro=raw_input("pls input ansible group:")
import ansible.runner as arun
import gobal_fun
def get_info():
   ass_list=[]
   runner = arun.Runner(
           module_name='setup',
	   module_args='',
           pattern='%s'%gro,
           forks=10
          )
   results=runner.run()
   INFO=results['contacted']
   for host,val in INFO.items():
	 for i in val['ansible_facts']["ansible_devices"]:
	     if i[0:2]  not in ("sr"):
		  dis=str(i+'_'+val['ansible_facts']['ansible_devices'][i]['size'])
	 ass=host,str(val['ansible_facts']["ansible_product_name"]),str(val['ansible_facts']["ansible_distribution"])+"_"+str(val['ansible_facts']["ansible_distribution_version"]),str(val['ansible_facts']['ansible_processor'][0]),str(val['ansible_facts']["ansible_processor_count"]),str(val['ansible_facts']["ansible_processor_vcpus"]),str(val['ansible_facts']["ansible_memtotal_mb"]),str(val['ansible_facts']['ansible_swaptotal_mb']),dis,str(val['ansible_facts']['ansible_default_ipv4']['address']),str(val['ansible_facts']['ansible_default_ipv4']['macaddress']),str(val['ansible_facts']['ansible_product_serial'])
	 ass_list.append(ass)
   #for i in ass_list:
   #    print i
   Msql="INSERT INTO `ansible_host` (`hostname`,`manufacturer`,`os`,`cpu_model`,`cpu_count`,`cpu_core`,`memory_totally`,`swap_totally`,`disk`,`ip`,`mac_address`,`sn`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   try:
      gobal_fun.cur.executemany(Msql,ass_list)
      gobal_fun.conn.commit()
      gobal_fun.cur.close()
      gobal_fun.conn.close()
      print "success insert "
   except Exceptioin,e:
      conn.rollback()
      print e
if __name__ == "__main__":
    get_info()
